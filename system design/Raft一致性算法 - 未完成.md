# 初衷
- 必须提供一个完整的实际的系统实现基础，这样才能大大减少开发者的工作
- 安全 & 高可用
- 高效率
- 可理解
# Paxos算法存在的问题
- 复杂，晦涩难懂
- 理论和实现之间有巨大的鸿沟

# 如何评估可理解？
手段1: 分治法： 只要有可能，我们就将问题分解成几个相对独立的，可被解决的、可解释的和可理解的子问题。Raft 算法被我们分成领导人选举（随机化去简化 Raft 中领导人选举算法），日志复制，安全性和角色改变几个部分。
手段2: 通过减少状态的数量来简化需要考虑的状态空间，使得系统更加连贯并且在可能的时候消除不确定性。
# Raft 一致性算法
领导人集中管理，复制日志的责任来实现一致性，把日志条目复制到其他服务器上，并且当**保证安全性的时候**告诉其他的服务器应用日志条目到他们的状态机中。
## Raft为了解决`可理解`的问题，把问题分成了三个阶段：
**领导选举**
当现存的领导人宕机的时候, 一个新的领导人需要被选举出来。
**日志复制**
领导人必须从客户端接收日志条目(log entries)然后复制到集群中的其他节点，并且强制要求其他节点的日志保持和自己相同（怎么保证？）。
**安全性**
在 Raft 中安全性的关键是在图 3 中展示的状态机安全：如果有任何的服务器节点已经应用了一个确定的日志条目到它的状态机中，那么其他服务器节点不能在同一个日志索引位置应用一个不同的指令。
## Raft中的概念
### Raft 集群的大小
集群内的机器数量可以自由定义，通常为5个。5个节点可以容忍两个节点的宕机，这在一般的实践场景中已经足够， 同一时刻出现3个机器的宕机概率很小， 只要不出现三台机器同时失效的情况， 系统都可以正常对外提供服务。 如果集群内的机器数量过大, 可能会降低整个系统对客户端的指令处理速度( 因为要复制更多数据,协调更多数据的一致性)
### 集群中节点的角色
**leader节点** -  leader 负责接收、处理、响应所有来自客户端的请求
**follower 节点** 
- 自己不发请求，只响应来自leader 和 candidate的请求
- 不响应其他follower发送的请求
- client发过来的请求，会把leader信息发送给client，让client去联系leader节点
**candidate 节点**
- candidate 是选举过程中的节点角色， 当 leader 失效后， 会有follower 转变为 candidate , 下一个 leader 从candidate 中产生。
![][image-1] 
集群刚刚启动时， 所有结点都是 follower，当 follower 收不到主结点发来的心跳时， 就会转变为 candidate，发起 leader 选举流程。 当一个 candidate 收集了集群中半数以上结点的选票后， 就能变成 leader。 一个 leader 会持续运行直到自己宕机或者发现其他拥有更高任期 （term） 的 leader。 term 的概念在后文中定义。
### Raft集群中的时间
![][image-2]
Raft 将系统内的时间划分成一段一段的任期（term)
- 每一个 term 的开始阶段都是选举过程， 在选举过程中， 会出现一个或多个候选人（candidate) 竞选 leader 的情形。在一次成功的选举后， 竞选成功的 leader 将会一直管理着整个集群直到下一个 term 出现。
- 有时， 竞选过程可能存在平票的情况， 即有有多个竞选人获得了相同数量的选票， 在这种情况下， 没有选出 leader，那么这个 term 就会直接结束，下一个 term 会进行新的选举
- Raft 算法会确保每一个 term 最多只有一位 leader 。
\<Time, clocks, and the ordering of events in a distributed system\>
#### term的工作流程
每一个服务器都有一个`current_term`的变量，该变量只允许增大，不允许被减小。
集群中每个服务器对外发送请求时都会带上`current_term`，
每个服务器 S 在收到任意请求时， 会先比较自己保存的` current_term `和收到的请求中携带的 `current_item`（记为`current_item_other`）的大小
```python
if current_item > current_item_other:
	# 拒绝请求
elif current_item < current_item_other:
	current_item = current_item_other
	state = follower # candidate 退化成follower
else:
	# 正常处理请求？？

```

### 集群中的通信方式
RPC
- RequestVoteRPC： 由竞选过程中的 candidates 发起调用， 用于收集选票
- AppendEntriesRPC： 由 leader 发起调用， 用于将指令 log 分发到各台服务器上或者作为心跳通知使用
#### 问题
超时
- 重试
一次性多个rpc调用，并发执行
### 如何选举Leader
触发时机
- 主节点宕机，follower 通过**心跳机制**检测到主节点宕机。
- 初次启动的时候。
#### 第一次启动
全部的节点都是follower，一台follower只要收到来自leader 或 candidate 的RPC调用，就会保持自己的follower身份。Leader 会向所有的 follower 定时发送心跳（ 也就是不携带数据的 **AppendEntriesRPC**）以维持他的权威。 如果一个 follower 在一段时间后（ `election_timeout`) 一直没有收到任何 **RPC** 调用请求， 它就会认为当前集群没有有效的 leader , 发起一轮新的选举。
#### 主节点宕机，follower 发起的选举
```python
# step1: current_term = current_term + 1
#        state = candidate
# step2: 给自己投一票，并向集群中所有其他服务器发起 RequestVoteRPC 并发调用
# 可能的结果：
# 1. 被选举为leader
# 2. 有其他服务器当选 leader ， 自己竞选失败
# 3. 一段时间过去后， 没有服务器当选 leader, 自己也没有竞选成功 
```
##### 赢得选举
收集到的票数大于总票数的一半，就会赢的选举。
每一个 follower 在某个特定的 term 中， 只会投出一张选票， 投票的原则是”先到先得“：最先收到哪一个 candidate 的 RequestVoteRPC 调用， 就将选票投给它。
 
收集半数以上选票才能竞选成功这一规则确保了同一个 term 中至多只会产生 1 个 leader 。一旦一个 candiate 赢得选举后， 它就会向集群内其他服务器发送心跳， 以此维持它的权威并且避免其他服务器发起新一轮选举。
##### 竞选失败
在赢得选举前（收集到票数\<= 总票数的一半）
收到了其他自称leader的节点发送的**AppendEntriesRPC**，请求会携带`current_item`，我们将它记为`current_item_other`。
本机也会保存一个 `current_item`
```python
if current_item > current_item_other:
	return refuse # 拒绝
elif current_item == current_item_other:
	return normal operation
else:
	current_item = current_item_other
	state = follower   # 降级成follower ，竞选失败
	return
```
##### 平票
如果最终有多个节点收集到的票数一致，无法选举出leader，那么，就会触发下一轮的选举，但是**平票**现象可能一直持续下去。
解决的办法：随机超时时间， 每一个服务器的超时时间都是在一个范围内随机选择的（例如100-300ms)。 如果继续平票，继续随机超时时间。发起下一轮选举前， 先等待 `election_timeout `中所设置的时长， 以此减少下一轮再次出现多个 candidate 平票的可能
### 如何分发 Command Log
- append `log entry` 到command log文件的末尾
- 对follower并行发起 AppendEntriesRPC 调用
- log entry 被**安全**的复制到所有的follower时，执行日志中的命令
- 返回执行结果给客户端
问题：follower 因为宕机、运行缓慢、或者网络数据通信丢包等问题导致 leader 发出的 AppendEntriesRPC 调用没有得到响应
处理方案：leader 会不限次数地一直进行重试直到所有的 follower 都存储了相同的 log 记录。



引用
[https://blog.csdn.net/lengxiao1993/article/details/108524808][1]
[https://github.com/maemual/raft-zh\_cn/blob/master/raft-zh\_cn.md][2]

[1]:	https://blog.csdn.net/lengxiao1993/article/details/108524808
[2]:	https://github.com/maemual/raft-zh_cn/blob/master/raft-zh_cn.md

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gsf9akys3yj30nw0g2wht.jpg
[image-2]:	https://tva1.sinaimg.cn/large/008i3skNly1gsf9d3iekcj30ng0esmzo.jpg