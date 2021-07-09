TinyURL
## 功能需求
1. 确定是实现一个服务还是一个算法 — 服务
2. 给定一个URL，服务需要生成一个短链地址
3. 根据短链  — 返回长链
4. 用户可以指定短链
5. 短链的时效性，短链存在过期时间，也可以主动指定过期时间
## 非功能需求
系统应该高可用，required
延迟：低延迟
安全性：无法猜测
数据的持久性：写入不能丢失
## 容量评估
系统特征：读多写少；
更多的是重定向的请求，假设读写比例为100:1。
流量评估：500,000,000 每月的新URL生成
- 新生成URL的QPS：200 URLs/s        — 读写服务分离
- URLs 重定向 ：20K URLs/s  
	存储评估：以5年为单位（多数公司活不过5年吗） - 15TB - 需要sharding
```python
500million * 5year * 12 months = 30 billion
```
假设每条记录占用500个字节，我们大概需要15T的存储：
```python
30 billion * 500 bytes = 15 TB
```

带宽评估 - 10M/s
```python
写：qps * 500 bytes = 200 * 500 bytes = 100kb/s
读：10M/s
```

内存评估 - 170G - 需要sharding
存储热点URLS，按照二八法则，我们20%的URL贡献了80%的流量
```python
19k * 3600 * 24 = 1.7 billion
要缓存 20% 的请求：我们大概需要170G的内存
0.2 * 1.7 billion * 500 字节 ～=170GB
```
## 服务设计-系统API
创建URL
```python
 def creatURL(api_dev_key, original_url, custom_alias=None, user_name=None, expire_date=None) -> str:
	# todo
	pass
"""
api_dev_key: str. 密钥，每个账户分配一个，可以用来限流
original_url: str.长链
custom_alias: str. custom 指定的key
user_name: 用于编码的用户名
expire_date: 短链过期日期

返回值：新生成的短链
"""
```
获取URL
```python
def getURL(api_dev_key, short_key) -> str:
	pass

```
## 存储
k-v存储，可以使用NoSQL数据库，例如TiDB存储
QPS 为200，单机就可以存储。
但是，数据量比较大，需要sharding
### 数据分区的策略
两种sharding 方式：
第一种：按照范围分。按照key的首个字符的（或者首两个字符）
优点：支持高效的范围查询（这个场景下的范围查询可以忽略）。
缺点：容易造成数据倾斜和访问倾斜。
第二种：按照hash分。
优点：数据分布比较均匀，访问也比较均匀。
缺点：范围查询支持性比较差（这个业务场景下的范围查询可以忽略）。
### 如何解决增加节点、删除节点导致大量数据迁移的问题？
一致性hash算法。
## 如何高效的生成短链？
### 短链的长度？
6个字符，字符的范围为62个字符，6^62次方个。
### 生成短链的方法
短链可以通过根据长链MurMurMur3对长链进行hash的方式产生。然后，基于base62进行编码。
### 检查是否存在以及处理碰撞
可用布隆过滤器检查短链是否存在（存在一定的误判率），如果存在，可以通过添加随机字符串的形式rehash。
### 如果选择雪花算法，怎么解决时钟漂移问题？
定时向注册中心写入自己时钟的时间，如果当前时间 和 上次写入的时间存在偏差，认为存在时钟漂移，等过了上一个时间再处理。
消费未来时间？？百度的方案 - 看下细节

## 如何优化读取速度？
缓存
### 需要多少内存？
20%的数据贡献了80%的流量，所以，可以使用LRU策略进行数据的驱逐。
### 选择哪一种驱逐策略？你还了解哪些驱逐策略？各有什么优缺点？
因为缓存的是热点数据，所以可以使用LRU策略。
lc 代码：[https://leetcode-cn.com/problems/lru-cache/][1]
相关驱逐策略，参考“缓存驱逐策略”
### 缓存和数据的一致性怎么保证？cache aside 策略
参考“cache-aside pattern”
## 如何限流？
参考 “限流”
## 长链访问信息统计
属于OLAP的范畴
## 安全性问题
### 预防措施
针对存量的短网址
- 增加单IP的访问频率和单IP访问总量的限制，超过阈值进行封禁。
- 对包含权限、敏感信息的短网址进行过期处理。
- 对包含权限、敏感信息的长网址增加二次鉴权。
针对增量的短网址
- 不利用短网址服务转化任何包含敏感信息、权限的短网址。
- 尽量避免使用token等验证方式。
# 引用
[https://security.tencent.com/index.php/blog/msg/126][2]
[https://edu.heibai.org/%E7%9F%AD%E7%BD%91%E5%9D%80%E7%9A%84%E6%94%BB%E5%87%BB%E4%B8%8E%E9%98%B2%E5%BE%A1.pdf][3]

[1]:	https://leetcode-cn.com/problems/lru-cache/
[2]:	https://security.tencent.com/index.php/blog/msg/126
[3]:	https://edu.heibai.org/%E7%9F%AD%E7%BD%91%E5%9D%80%E7%9A%84%E6%94%BB%E5%87%BB%E4%B8%8E%E9%98%B2%E5%BE%A1.pdf