news Feed design
新鲜事系统设计
## 功能需求
### 场景（用例）
可以逐条列出你能想到该系统应该具备哪些功能，询问面试官要设计哪个功能。
例如：在新鲜事系统中，可能存在的功能点：
- 用户注册、登陆
- 用户详情信息/ 编辑
- 上传文件/视频
- 搜索
- 发推文
- 新鲜事（Timeline / News Feed）
- 关注、评论、点赞、转发
- 关注/取关
核心功能：用户获取和发布新鲜事
流程：
![][image-1]

## 非功能需求
找到可能影响流程中性能的因素。
这块重要的不是计算的结果，而是**过程**，你能根据一些指标推算出QPS。
为什么需要了解QPS？
- QPS = 100 
	- 笔记本就可以满足需求
- QPS = 1000 
	- 用一台好点的web服务器就能满足，需要考虑单点问题
- QPS = 1百万
	- 需要1000台web集群
	- 需要考虑如果维护这个集群
QPS 和 WebServer 、DB的关系
- 一台WebServer大约承受1k的QPS（考虑逻辑处理和DB的查询）
- 一台SQL DB大约承受1k的QPS（考虑到逻辑处理时间和数据查询时间）
- 一台NoSQL DB大约承受10k的QPS
- 一台NoSQL DB（memcached Redis）大约承受10万+的QPS。
### 指标
- DAU（日活）：假设日活跃用户为3亿（twitter日活），50% ～70%的月活
-  QPS：DAU * 每个用户平均请求次数 / 3600 * 24 = 100k 
- 峰值：QPS * 3 ，3 是一个估计的数字，也可以是其他数字，快速增长的产品可以将3这个系数调的更大一点。
通过上面的估计的参数，可以估算到DB的读写QPS。
- 读频率（read QPS，queries per second）：300k
- 写频率：5k 
> > 读多写少，考虑索引索引结构为B树的DB，eg: MySQL，MongoDB
> > 写多读少，考虑基于LSM存储引擎的数据库，LevelDB，RocksDB
## 高层设计
先给出一个可以用的设计方案，然后在此基础上和面试官讨论，进行逐步优化。
### 服务拆分
- 用户中心（user service）：注册/登陆
-  用户关系（relationship）：关注/取关
- news中心  （news service）：发布消息、news feed 、timeline
-  Media 服务（media service）：upload image、upload video
![][image-2]
### 存储 
**如何选择合适的存储结构？**

用户信息属于结构化信息，选用MySQL存储。
DB Schema 
```sql
# 用户表 user
	# 字段
		user_id int
		name varchar(64)
		created_at datetime
		last_modified datetime
# 用户关系表 relationship
	# 字段
		followee_id
	    follower_id
	
# news表 news
	# 字段
		news_id bigint
		content 
		user_id
		created_at datetime
```
Media信息存储在NoSQL数据库中（MongoDB、对象存储）。
### API 设计
```python
# 获取关注者（followers）
def getFollowees(followee: int) -> List[int]:
	pass

# 获取关注者的推文数据，并排序，获取当前页数据(假设1页为20个)
def getNews(followees: List[int], page=20, filters: Dict[str, str]) -> List[int]:
	pass
```
#### 如何获取news feed？
##### 方案1： Pull模型
![][image-3]
- 获取关注对象：
```sql
select followee_id from relation where follower_id = 'zhangsan';
```
- 获取新鲜事（k路归并）
```sql
select news_id, content from news where user_id = '' order by created_at desc limit 20;

# 对所有news 做排序，然后取前20条
```
缺点：数据规模单表上千万时，关注对象比较多时，延时会增加，影响用户体验。
##### 方案2: push 模型
设计一个表，记录每个用户应该看到的news，属于结构化信息，选用MySQL存储。
算法：
- 为每个用户建一个list存储存储news Feed消息
	- 用户发一个news后，将该消息推送到用户的所有粉丝的News Feed List
	- 用户要查看News Feed时，只需要查询格子布的News Feed List
复杂度：
News Feed： 一次读取
Post News：N个粉丝，N次写入，但是可以使用异步的方式写入

DB Schema
```sql
# news feeds 表
	id
	news_id  
	owner_id
	created_at
```

缺点：
1. 大V问题。当用户有2000万粉丝时，即使异步，也可能得好几个小时他的所有粉丝才能看到消息，这个是不能接受的。
2. 僵尸粉的问题
3. 需要更多的存储空间
### 发布一条消息？
往news 表中插入一条记录。

## 可扩展设计（深入分析）
选用Pull模型，因为大V问题解决起来更困难。

### 针对Pull模型的优化
因为最慢的部分发生在用户读请求时
- 在DB的前面添加Cache
- Cache 每个用户的TimeLine
	- N次DB请求 -\> N 次Cache请求（N为关注的好友数量）
	- Tradeoff：要cache 所有的news吗？
- Cache 每个用户的News Feeds
	- 没有Cache News Feed 的用户：需要获取n个用户的最近20条news，merge，然后取前20条
	- Cache News Feed的用户：归并n个用户在某个时间戳之后的所有news。
### 如果选择Push模型，怎么优化？
磁盘空间的问题：不是问题。
僵尸粉问题：粉丝权重排序（将僵尸粉最后处理）
大V问题：很难解决。可以同时使用push模型和pull模型。
## 注意事项
- 不要在方案之间来回摇摆
- 尽量在现有的模型下，做最小的改动来优化
- 对长期增长做一个评估，评估是否值得转换整个模型

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gqgmw967b4j312k05c43a.jpg
[image-2]:	https://tva1.sinaimg.cn/large/008i3skNly1gqgsc41jk1j31500ectfk.jpg
[image-3]:	https://tva1.sinaimg.cn/large/008i3skNly1gqgmw967b4j312k05c43a.jpg