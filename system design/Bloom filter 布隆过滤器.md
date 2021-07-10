# 什么是Bloom filter
Bloom Filter 是一种数据结构，它可以用来判断某个元素是否在集合内，特点是**运行速度快**，**占用内存小**。
布隆过滤器流行背后的很大一部分原因是，它们是一种设计和实现起来相当简单的数据结构，同时在许多情况下也非常有用。虽然是20世纪70年代发明的，但是在过去几十年里随着各领域大量数据的涌现，它才声名大噪。
# 它是如何工作的
布隆过滤器本身并不存储项目，它们使用的空间小于正确存储数据所需的理论下限，因此，它们存在误判率。它们有“false positives”，但没有“false negatives“，这种错误的片面性可以转为对我们有利。
![][image-1]
因此，在查询答案被预期为 "不存在 "的情况下，布隆过滤器在大多数时候都能提供很高的准确性，而且还能节省空间。
Bloom filter 里的哈希函数需要是彼此独立且均匀分布，它们也需要尽可能的快。
快速，简单且彼此独立的哈希函数的例子：
包括 [murmur][1], [fnv][2] 族哈希函数, 以及[HashMix][3]。当把 bloom filter 的实现从 md5 切换到 murmur 时，速度提升了 800%。
- Chromium 使用 HashMix. (同时, 这里 是一个简短说明他们如何使用 bloom filter）
- [python-bloomfilter][4] 使用加密哈希算法。
- Plan9 使用一种简单的哈希算法，Mitzenmacher 2005
- [Sdroege Bloom filter][5] 使用 fnv1a (把这个加进来是希望展示有人使用 fnv 算法)
- [Squid][6] 使用 MD5

## 插入
一个布隆过滤器有两个主要组成部分：
- 一个比特数组A[0...m-1]()，所有的槽最初都设置为0；
- k个独立的哈希函数h1,h2,...,hk,每个都均匀随机地将密钥映射到一个范围[0,m-1]()。

为了将一个数据 x 插入到布隆过滤器中，我们首先计算 x 上的 k 个哈希函数，对于每个产生的哈希值，将 A 的相应槽设置为 1（见下面的伪代码和图2）。
```python
Bloom_insert(x):
 for i ← 1 to k 
        A[hi(x)] ←1
```
时间复杂度：O(k)
## 查询
与插入类似，查找在 x 上计算 k 个哈希函数，第一次 A 的对应槽之一等于 0 时，查找报告该项目为不存在，否则报告该项目为存在（以下伪代码）。
```python
Bloom_lookup(x):
 for i ← 1 to k 
       if(A[hi(x)] = 0)
       return NOT PRESENT
 return PRESENT
```
时间复杂度：O(k)

### Bloom filter 容量
布隆过滤器可以通过调整过滤器的大小来调整准确率。一个大的过滤器会拥有比一个小的过滤器更低的错误率。
错误率的计算公式：
![][image-2]
其中：
- m为比特阵列的大小
- k为哈希函数的数量
- n为预期插入过滤器的元素数量
- false activiry的概率P
可见，m越大，k越大，P越小

###   hash 函数的数量
hash函数多了，插入和查询时的效率越差。
hash函数少了，误判率就会变高。
```python
借助公式：(m/n)ln(2)
```
[可以通过以下的步骤来确定 Bloom filter 的大小:][9]
- 确定 n 的变动范围
- 选定 m 的值
- 计算 k 的最优值
- 对于给定的n, m, and k计算错误率。如果这个错误率不能接收，那么回到第二步，否则结束
# 案例
例如，[谷歌的Webtable][10]和[Apache Cassandra][11]就是这样使用布隆过滤器的，它们是最广泛使用的分布式存储系统，旨在处理大量数据。也就是说，这些系统将其数据组织到一些被称为分类字符串表（SST）的表中，这些表位于磁盘上，结构为键值图。在Webtable中，键可能是网站名称，而值可能是网站属性或内容。在Cassandra中，数据的类型取决于什么系统在使用它，因此，例如对于Twitter，键可能是用户ID，而值可能是用户的推文。
当用户查询数据时，会出现一个问题，因为我们不知道哪个表包含了所需的结果。为了帮助定位正确的表而不在磁盘上明确检查，我们在RAM中为每个表维护一个专用的Bloom过滤器，并使用它们将查询路由到正确的表，其方式如图1所述。
![][image-3]
图1：分布式存储系统中的布隆过滤器
在这个例子中，我们在磁盘上有50个排序的字符串表（SST），每个表都有一个专门的布鲁姆过滤器，由于其体积小得多，所以可以放入RAM。当用户进行查询时，查询首先会检查布隆过滤器。在这个例子中，第一个报告项目为存在的Bloom filter是Bloom filter No.3。然后我们继续在磁盘上的SST3中检查该项目是否存在。在这种情况下，这是一个错误的警报。我们继续检查，直到另一个布隆过滤器报告存在。布隆过滤器第50号报告存在，我们就去磁盘上实际定位并返回所请求的项目
[点击查看更多的案例][12]

# 引用
[https://llimllib.github.io/bloomfilter-tutorial/zh\_CN/][13]
[https://freecontent.manning.com/all-about-bloom-filters/][14]
[https://mightguy.medium.com/bloomfilter-in-searchengine-part-i-2f34814894b9][15]

[1]:	https://sites.google.com/site/murmurhash/
[2]:	http://isthe.com/chongo/tech/comp/fnv/
[3]:	http://www.google.com/codesearch/url?ct=ext&url=http://www.concentric.net/~Ttwang/tech/inthash.htm&usg=AFQjCNEBOwEAd_jb5vYSckmG7OxrkeQhLA
[4]:	https://github.com/jaybaird/python-bloomfilter/blob/master/pybloom/pybloom.py
[5]:	https://github.com/sdroege/snippets/blob/master/snippets/bloomfilter.c
[6]:	http://google.com/codesearch/p?hl=en#GUxBL_cNJpE/src/store_key_md5.c&q=bloom%20package:squid&d=1
[9]:	https://llimllib.github.io/bloomfilter-tutorial/zh%5C_CN/
[10]:	https://freecontent.manning.com/all-about-bloom-filters/#id_ftn3
[11]:	https://freecontent.manning.com/all-about-bloom-filters/#id_ftn4
[12]:	https://freecontent.manning.com/all-about-bloom-filters/
[13]:	https://llimllib.github.io/bloomfilter-tutorial/zh_CN/
[14]:	https://freecontent.manning.com/all-about-bloom-filters/
[15]:	https://mightguy.medium.com/bloomfilter-in-searchengine-part-i-2f34814894b9

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gsbrc7r743j30q00esq3i.jpg
[image-2]:	https://tva1.sinaimg.cn/large/008i3skNly1gsbsnncwjcj30ik060wf4.jpg
[image-3]:	https://tva1.sinaimg.cn/large/008i3skNly1gsbrg2msf0j30fx0ozwi7.jpg