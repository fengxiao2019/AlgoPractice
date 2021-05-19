一致性hash算法
主要应用领域：负载均衡。
场景：假设现在有TB级别的数据，采用hash 关键字分区的方式，数据保存到100个节点上。
## **方案1**
`nodeNum`: 表示节点的个数
`key` : 表示分区关键字
确定key在哪个节点的算法
	hash_function(key) % nodeNum
	"""
	因为hash结果值都比较大，所以可以采用逐位取模的方式
	"""
	def getHexStrMode(hex_str, mod_num):
	    str_len = len(hex_str)
	    result_mod = 0
	    for idx, ch in enumerate(hex_str):
	        result_mod = (result_mod * 16 + int(ch, 16)) % mod_num
	    return result_mod
缺点：
> 节点数量可能频繁变化，导致数据迁移比较频繁
> 节点故障时，单次迁移的数据量比较大
## 方案2
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
	3. 数据迁移压力大，当新增节点时，需要从附近的两台机器迁移数据到新机器，两台老机器承担了较大的数据迁移压力，其他机器无法承担迁移压力。
## 方案3- 一致性hash算法
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