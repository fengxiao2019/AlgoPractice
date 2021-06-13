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
 def creatURL(api_dev_key, original_url, custom_alias=None user_name=None,expire_date=None) -> str:
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
