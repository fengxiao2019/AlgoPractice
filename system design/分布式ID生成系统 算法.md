业务系统中设计分布式ID你需要考虑的因素包括：
1. 全局唯一性：最基本的要求
2. 趋势递增：假设分布式ID作为主键存储，在MySQL InnoDB存储引擎下，为了保证写入的高效，分布式ID需要具备趋势递增的特性。
3. 单调递增：保证下一个ID一定大于上一个ID，例如事务版本号、IM增量消息、排序等特殊需求。
4. 信息安全：如果分布式ID完全连续会可能导致恶意用户爬取工作非常容易，如果是订单信息，可能更危险。
非功能需求：
1. 延迟要尽可能的低。200ms内
2. 可用性达到5个9（如果提高系统的可用性？冗余+备份+系统保护（限流+熔断））
## 算法
### UUID
UUID(Universally Unique Identifier)的标准型式包含32个16进制数字，以连字号分为五段，形式为8-4-4-4-12的36个字符，示例：550e8400-e29b-41d4-a716-446655440000，到目前为止业界一共有5种方式生成UUID。
优点：
性能非常高：本地生成，没有网络消耗。
缺点：
- 不易于存储：UUID太长，16字节128位，通常以36长度的字符串表示，很多场景不适用。
- 信息不安全：基于MAC地址生成UUID的算法可能会造成MAC地址泄露（版本1和版本2）。
- ID作为主键时在特定的环境会存在一些问题，比如做DB主键的场景下，UUID就非常不适用
### 类snowflake方案
![][image-1]
特征：
- 首位为0，保证正数
- 41位时间戳，可以使用69年
- 10个bits，表示1024个机器
- 12个bits，自增序列号
支持自定义，例如，10个bits可以根据业务场景再次切分。
理论上snowflake方案的QPS约为409.6w/s，这种分配方式可以保证在任何一个IDC的任何一台机器在任意毫秒内生成的ID都是不同的。
优点：
- 毫秒数在高位，自增序列在低位，整个ID都是趋势递增的。
- 不依赖数据库等第三方系统，以服务的方式部署，稳定性更高，生成ID的性能也是非常高的。
- 可以根据自身业务特性分配bit位，非常灵活。
缺点：
- 强依赖机器时钟，如果机器上时钟回拨，会导致发号重复或者服务会处于不可用状态。
[MongoDB中ObjectID的生成方案：][1]
> Returns a new ObjectId value. The 12-byte ObjectId value consists of:
> - a 4-byte timestamp value, representing the ObjectId's creation, measured in seconds since the Unix epoch
> - a 5-byte random value
> - a 3-byte incrementing counter, initialized to a random value
> While the BSON format itself is little-endian, the timestamp and counter values are big-endian, with the most significant bytes appearing first in the byte sequence.
### [数据库生成（Redis or MySQL）][2]
以MySQL举例，利用给字段设置auto\_increment\_increment和auto\_increment\_offset来保证ID自增，每次业务使用下列SQL读写MySQL得到ID号。
```sql
begin;
REPLACE INTO Tickets64 (stub) VALUES ('a');
SELECT LAST_INSERT_ID();
commit;
```
优点：
- 非常简单，利用现有数据库系统的功能实现，成本小，有DBA专业维护。
- ID号单调自增，可以实现一些对ID有特殊要求的业务。
缺点：
- 强依赖DB，当DB异常时整个系统不可用，属于致命问题。配置主从复制可以尽可能的增加可用性，但是数据一致性在特殊情况下难以保证。主从切换时的不一致可能会导致重复发号。
- ID发号性能瓶颈限制在单台MySQL的读写性能。
性能问题的解决方案：
在分布式系统中我们可以多部署几台机器，每台机器设置不同的初始值，且步长和机器数相等。比如有两台机器。设置步长step为2，TicketServer1的初始值为1（1，3，5，7，9，11…）、TicketServer2的初始值为2（2，4，6，8，10…）。
```sql
TicketServer1:
auto-increment-increment = 2
auto-increment-offset = 1

TicketServer2:
auto-increment-increment = 2
auto-increment-offset = 2
```
缺点：
- 水平扩展困难。
- ID没有了单调递增的特性，只能趋势递增，这个缺点对于一般业务需求不是很重要，可以容忍。
- 数据库压力还是很大，每次获取ID都得读写一次数据库，只能靠堆机器来提高性能。

### 美团的Leaf-Segment 数据库方案
在数据库方案的基础上做了优化。原方案每次获取ID都得读写一次数据库，造成数据库压力大。改为利用proxy server批量获取，每次获取一个segment(step决定大小)号段的值。
用完之后再去数据库获取新的号段，可以大大的减轻数据库的压力。 - 各个业务不同的发号需求用biz\_tag字段来区分，每个biz-tag的ID获取相互隔离，互不影响。如果以后有性能需求需要对数据库扩容，不需要上述描述的复杂的扩容操作，只需要对 biz\_tag 分库分表就行。
![][image-2]
字段说明：
biz_tag 区分业务，业务标签
max_id表示该biz_tag目前所被分配的ID号段的最大值。
step表示每次分配的号段长度。
```sql
Begin
UPDATE table SET max_id=max_id+step WHERE biz_tag=xxx
SELECT tag, max_id, step FROM table WHERE biz_tag=xxx
Commit
```
优点：
- 横向扩展非常容易，性能完全能够支撑大多数业务场景。
- ID号码是趋势递增的8byte的64位数字，满足上述数据库存储的主键要求。
- 容灾性高：**Leaf服务内部有号段缓存**，即使DB宕机，短时间内Leaf仍能正常对外提供服务。
- 可以自定义max_id的大小，非常方便业务从原有的ID方式上迁移过来。
缺点：
- 1.**ID号码不够随机**，能够泄露发号数量的信息，不太安全。
- 2.DB宕机会导致整个系统不可用（可以使用db的高可用配置（半同步、类Paxos算法”实现的强一致MySQL方案））。
- 3.任一节点的号段耗尽时都需要从 DB 中取出下一个号段再返回 ID ，这个延迟会造成一定的请求毛刺。
优化点：可以使用双buffer，当其中一个 buffer 消耗到一定阈值时，异步更新下一个 buffer，这个阈值是可调整的。 buffer 太长有坏处，如果程序异常退出、正常重启，buffer 太长很容易造成巨大的 ID 空洞。一个号段的使用时间是由消费速度和 buffer 长度决定的。为了尽最大可能提升可用性， buffer 自然是越长越好，这样在 DB 出问题时，我们还能抗一段时间。

### 美团的Leaf-snowflake方案
Leaf-segment方案可以生成**趋势递增的ID**，**同时ID号是可计算的**，**不适用于订单ID生成场景**，比如竞对在两天中午12点分别下单，通过订单id号相减就能大致计算出公司一天的订单量，这个是不能忍受的。
#### 如何解决时钟回拨问题？
服务启动时首先检查自己是否写～ZooKeeper leaf_forever节点。
如果写过，对比机器和时间和 ZooKeeper leaf_forever 中存储的时间，如果差距比较大，说明，回拨严重，需要上报告警。
如果没有写过， 写入，并且通过rpc 获取其它节点的时间，取中间值判断差值是否在可接受的范围内，如果在范围内，正常启动，否则，报警。
每隔一段时间(3s)上报自身系统时间写入leaf_forever/${self}。
[伴鱼也是类似的处理方式][3]
### [百度的UIDGenerator方案][4]
基于Snowflake算法的唯一ID生成器，通过消费未来时间克服了雪花算法的并发限制。UidGenerator提前生成ID并缓存在RingBuffer中。 单个实例的QPS能超过6000,000。
![][image-3]
可以根据不同的业务需求，调整各个部分占用的bits数量。
UidGenerator提供两种方式：DefaultUidGenerator 和 CachedUidGenerator 。
#### workid 的生成
```sql
DROP TABLE IF EXISTS WORKER_NODE;
CREATE TABLE WORKER_NODE(
  ID BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  HOST_NAME VARCHAR(64) NOT NULL COMMENT 'host name',
  PORT VARCHAR(64) NOT NULL COMMENT 'port',
  TYPE INT NOT NULL COMMENT 'node type: ACTUAL or CONTAINER',
  LAUNCH_DATE DATE NOT NULL COMMENT 'launch date',
  MODIFIED DATETIME NOT NULL COMMENT 'modified time',
  CREATED DATEIMTE NOT NULL COMMENT 'created time'
)
 COMMENT='DB WorkerID Assigner for UID Generator',ENGINE = INNODB;
```
分布式ID的实例启动的时候，往这个表中插入一行数据，得到的id值就是准备赋给workerId的值。由于workerId默认22位，那么，集成UidGenerator生成分布式ID的所有实例重启次数是不允许超过4194303次（即2^22-1），否则会抛出异常。 当然也可以自定义生成workerid的方式。
#### sequence
- synchronized保证线程安全；
- 如果时间有任何的回拨，那么直接抛出异常；
- 如果当前时间和上一次是同一秒时间，那么sequence自增。如果同一秒内自增值超过2^13-1，那么就会自旋等待下一秒（getNextSecond）；
- 如果是新的一秒，那么sequence重新从0开始
#### CachedUidGenerator
满足填充新的唯一ID条件时，通过时间值递增得到新的时间值（lastSecond.incrementAndGet()），而不是System.currentTimeMillis()这种方式，而lastSecond是AtomicLong类型，所以能保证线程安全问题。
“””todo”

引用[https://tech.meituan.com/2017/04/21/mt-leaf.html][5]

[1]:	https://docs.mongodb.com/v4.4/reference/method/ObjectId/
[2]:	https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-the-cheap/
[3]:	https://tech.ipalfish.com/blog/2020/08/09/id_gen/
[4]:	https://my.oschina.net/u/1000241/blog/3048980
[5]:	https://tech.meituan.com/2017/04/21/mt-leaf.html

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1grwunva1z0j30uw07uq3i.jpg
[image-2]:	https://tva1.sinaimg.cn/large/008i3skNly1grwwvvbwetj30s0064jsi.jpg
[image-3]:	https://tva1.sinaimg.cn/large/008i3skNly1grwyi2gewfj30ye08c76d.jpg