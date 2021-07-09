# cache-aside pattern
许多商业缓存系统提供了read-through 、write-through/write-behind策略，在这些系统中，一个应用程序通过引用缓存来检索数据。如果数据不在缓存中，它就会从数据存储中检索并添加到缓存中。对缓存中的数据的任何修改也会自动写回到数据存储中。

如果你使用的缓存不提供这样的功能，那就需要业务后端来维护缓存和DB的数据一致性，常用的策略就是cache-aside 模式。
![][image-1]
一致性问题。
实现Cache-Aside模式并不能保证数据存储和缓冲区之间的一致性。数据存储中的某条记录可能在任何时候被外部进程改变，而这个改变可能不会反映在缓存中（例如回写缓存失败），直到缓存中的这条记录过期或者因为其他原因失效。

场景：缓存用户信息，缓存时间1分钟。
更新用户信息的策略。
策略1: 删除缓存，更新DB。
策略2: 更新DB，删除缓存。**这种策略下，不一致的概率更低**。
策略3: 更新缓存，更新DB。
策略4: 更新DB，更新缓存。

解决办法：
如果是因为第三步回写失败的原因，可以利用消息队列重试机制进行补偿。
引用：
[https://docs.microsoft.com/en-us/azure/architecture/patterns/cache-aside][1]

[1]:	https://docs.microsoft.com/en-us/azure/architecture/patterns/cache-aside

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gqos97fdjxj30ym0msq62.jpg