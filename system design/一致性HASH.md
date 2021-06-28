一致性HASH
主要应用领域：负载均衡。
场景：假设现在有TB级别的数据，采用hash 关键字分区的方式，数据保存到100个节点上。
## **普通取模算法**
`nodeNum`: 表示节点的个数
`key` : 表示分区关键字
确定key在哪个节点的算法
```python
"""
hash_function(key) % nodeNum
因为hash结果值都比较大，所以可以采用逐位取模的方式
"""
def getHexStrMode(hex_str, mod_num):
    str_len = len(hex_str)
    result_mod = 0
    for idx, ch in enumerate(hex_str):
        result_mod = (result_mod * 16 + int(ch, 16)) % mod_num
    return result_mod
```
缺点：
> 它不具有水平扩展性。每当系统中增加一个新的缓存主机，所有现有的映射就会被破坏。如果缓存系统包含大量的数据，这将是一个维护的痛点。实际上，很难安排一个停机时间来更新所有的缓存映射。
> 它可能不是负载平衡的，特别是对于非均匀分布的数据。在实践中，可以很容易地假设数据不会被均匀地分布。对于缓存系统来说，这意味着一些缓存数据量大并且是热点数据，而其他的缓存则闲置和几乎为空。
## 一致性hash算法1
什么是一致性hash算法？
一致性hash算法是分布式缓存系统和DHTs的一个非常有用的策略。它允许将数据分布在一个集群中，当节点被添加或移除时，可以最大限度地减少数据迁移。因此，使缓存系统更容易扩大或缩小规模。
在一致性hash算法中，当hash表被调整大小时（例如，一个新的缓存主机被添加到系统中），只有k/n键需要被重新映射，其中k是键的总数，n是服务器的总数。回顾一下，在一个使用 "mod "作为散列函数的缓存系统中，所有的键都需要被重新映射。
在一致性hash表中，如果可能的话，对象会被映射到同一个主机上。当一个主机从系统中移除时，该主机上的数据被其他主机共享；而当一个新的主机被添加时，它从一些主机上获取它的份额，而不触及其他的份额。

方案1 中modNum会经常变化，可以采取固定modNum的方式，ModNum取一个很大的数，对应一个环，eg 2^32 - 1，对节点进行取模，将节点映射到环上，如下图所示。
对每个关键字进行hash，按顺时针方向寻找节点。
![][image-1]
当节点故障时，只有1/N分之一（N表示节点个数）的数据需要迁移。在下面的图中，当node1 故障时，只有node5～node1范围内的数据需要迁移。
![][image-2]
缺点：
1. 每个节点获取的数据可能非常不均匀。
![][image-3]
2. 在节点故障或者新增节点时，也会导致数据不均匀分布。
	![][image-4]
3.  数据迁移压力大，当新增节点时，需要从附近的两台机器迁移数据到新机器，两台老机器承担了较大的数据迁移压力，其他机器无法承担迁移压力。
## 方案3- 一致性hash算法 优化
将整个hash区间看作环，环的范围设置为2^64 - 1
同时将机器和数据都看作环上的点，引入Virtual nodes的概念，例如，一台实体机器对应1000个虚拟节点，每个virtual node 对应环上的一个点。这可以缓解数据分布不均匀的问题，同时降低数据迁移的规模。

增加一台实体机器：添加1000个虚拟节点，这1000个虚拟节点对应此实体机器。
如何确定数据应该在存储哪台机器上？
- 计算key的hash 值，得到一个0～2^64 - 1 范围内的值，对应环上的一个点
- 顺时针找到第一个virtual node
- 该virtual node 对应的实体机器就是key所在的数据库服务器
![][image-5]
新增加一个节点时，涉及到的数据迁移？
- 1000个virtual node 各自向顺时针的一个virtual node要数据

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gqmjkbel8xj30u20hignx.jpg
[image-2]:	https://tva1.sinaimg.cn/large/008i3skNly1gqmjmkskgwj30ui0ien00.jpg
[image-3]:	https://tva1.sinaimg.cn/large/008i3skNly1gqmkea9xrqj30nm0jadie.jpg
[image-4]:	https://tva1.sinaimg.cn/large/008i3skNly1gqmkj2kb1fj31400kmtdy.jpg
[image-5]:	https://tva1.sinaimg.cn/large/008i3skNly1gqmm8e4xg0j312a0mi44e.jpg