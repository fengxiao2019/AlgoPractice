# 需求
## 功能需求
- 上传/下载/分享图片 - 图片/视频的存储可以采用AZure Blob存储
- 图片/视频 timeline  - 用户-好友关系
- 根据图片标题搜索（如何做搜索）- 倒排索引
- 可以关注其他用户 - 关注/取关
## 非功能需求
- 高可用 - 
- 低延迟 - 200ms
- 数据的持久性 - 上传了文档不丢失
## 容量评估
- DAU     1 Million 
- 每日上传的文件的数量2 Million，每个文件的大小为200kb，平均每秒上传23个图片
- 计算存储空间 每天`2Million * 200k = 400GB`，5年需要存储容量712T

## System API

## High level design
![][image-1]
##  DB （schema, sql/nosql, sharding, replication）
- `photo_id`:`user_id`/`photo_path`/`photo_latitude`/`photo_longitude`/`created_time`/ `user_latitude`/`user_longitude`
- `user_id`: `name`/ `email`/ `created_time`/ `last_login`
- `relation`: `from`/ `to`  - 单向的关系
可以选择关系性数据库，也可以选用非关系性数据库。

## other topics
上传视频/大图片可能比较耗时，可以将写入和读分开处理。分开之后，可以单独优化。
### 高可用性
![][image-2]
#### 存储层面的高可用性
添加备份，数据怎么同步？可以采用semi-sync的方式进行主库-备库之间的同步。
#### 服务的高可用
服务添加冗余，去除单点
#### 数据的分区
按照`user_id`分区
- 存在热点问题，访问倾斜，或者存储倾斜
	解决的办法：热点`user_id`添加随机值存储到多个分区
按照`photo_id`分区
- 无法完全解决热点问题，但是概率要小很多
- 缺点是高频的查询某个用户`photo_id`遍历所有的分区
	解决的办法：缓存，将某个用户的下的photoid缓存起来。
#### 解决数据迁移的问题
一致性hash算法
### 生成Timeline
用户-关注的用户-最新的20条消息-k路归并
缺点：延迟可能会比较高，因为需要查询多张表，然后排序
改进方案：提前生成Timeline table，一个用户生成一条新的消息，查找关注他的人，然后写入Timeline Table，这样的话，只需要查询Timeline table就可以了。

#### pull 模型
客户可以定期或在他们需要的时候手动从服务器拉取时间线数据。这种方法可能存在的问题是：
-  新的数据可能不会显示给用户，直到客户发出pull请求
- 如果没有新的数据，大多数时候pull请求会导致一个空的响应，浪费资源
#### push 模型
服务器可以在新数据可用时立即推送给用户。为了有效地管理这一点，用户必须与服务器保持一个Long Poll（或者websocket）请求以接收更新。这种方法的一个可能的问题是：
- 当一个用户有大量的关注者或一个拥有数百万关注者的名人用户，在这种情况下，服务器必须相当频繁地推送更新。
**实现方式**
过程：查找用户关系-异步更新
查找用户关系-\> 可以用redis 有序集合缓存用户关系（key 为`user_id`, value为对应的`分数`，分数可以简单的设置为关注时间，也可以是其它更复杂的因子）
![][image-3]
#### 混合模式
我们可以采取一种混合方法。我们可以将所有拥有高关注度的用户转移到基于pull的模式，而只向那些拥有几百（或几千）关注度的用户采用push模式。

#### 影响排序的因素
- 您与好友、小组或主页所发布帖子的互动频率（好友和家人的帖子优先显示）。
- 帖子类型是否是您经常与之互动的类型（例如：照片、视频、链接）。
- 用户和主页在查看帖子后给出的评论、点赞、心情和分享数量。请注意，这些是您关注的好友、小组或主页所分享的帖子。
- 帖子发布后距离现在已过去多久时间。


引用
[https://www.webarchitects.io/system-design-question-design-facebooks-news-feed/][1]

[1]:	https://www.webarchitects.io/system-design-question-design-facebooks-news-feed/

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gsfh6ag1zaj30rk0r015e.jpg
[image-2]:	https://tva1.sinaimg.cn/large/008i3skNly1gsfdp09snbj315y0kygs0.jpg
[image-3]:	https://tva1.sinaimg.cn/large/008i3skNly1gsfhuapn4mj31060sm0wy.jpg