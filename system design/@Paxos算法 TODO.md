@Paxos算法 TODO
# 应用场景
- leader election
- group membership
- cluster management
- service discovery
- resource/access management
- consistent replication of the master nodes in services.
# 简单介绍
共识在没有故障发生的情况很容易达成，但是在有损信道、参与者可能宕机和时钟不同步等假设的情况下，问题会变得非常复杂。
Paxos协议是在1989年由Paxos提出的，但是直到2000年才谷歌的文件系统（GFS）使用Paxos实现了GFS锁服务，也就是Google Chubby，使得Paxos协议声名鹊起。
Google Chubby 的一个开源实现的版本是Apache ZooKeeper 项目ZooKeeper对Chubby接口稍作了概括，并为 "协调即服务 "提供了一个通用的可使用系统。ZooKeeper使用一个Paxos变体协议 Zab 来解决分布式共识问题。由于Zab被嵌入到ZooKeeper的实现中，它仍然是不清晰的，没有被采纳为一个通用的Paxos共识组件。Zab组件需要大量的工作来集成到应用程序中，但是ZooKeeper的即用型文件系统抽象接口得到了普及，成为云计算应用程序事实上的协调服务。然而，由于使用ZooKeeper接口的门槛很低，它已经被许多应用程序滥用/误用了。当ZooKeeper被不当使用时，它常常构成这些应用的性能瓶颈，并造成可扩展性问题。

最近Paxos协议和Paxos系统的数量迅速增长，为选择使用哪种共识/协调协议/系统增加了更多的选择。利用ZooKeeper，BookKeeper和Kafka 项目引入了日志/流复制服务。Raft协议回到了基本面，提供了Paxos协议的开源实现，作为一个可重用的组件。尽管Paxos协议和Paxos系统的选择和专业化程度不断提高，但对于这些系统的正确使用情况以及哪些系统更适合于哪些任务，仍然存在困惑。一个常见的误区是将Paxos协议与建立在这些协议之上的Paxos系统混为一谈（见图1）。Paxos协议（如Zab和Raft）对服务器复制的底层组件很有用，而Paxos系统（如ZooKeeper）经常被塞进这个任务中。Paxos系统的正确用例是在高可用/持久性的元数据管理方面。
![][image-1]
\# 
Zab算法有三个阶段，每个节点在任何时候都可以处于这三个阶段中的一个。**发现阶段**是发生领导者选举的地方，在当前已知的法定人数的配置上。一个进程只有在它有较高的纪元或纪元与较高的承诺交易ID相同时才能被选举。在**同步阶段**，新的领导者与所有追随者同步其前一个纪元的初始历史。只有在追随者的法定人数承认他们与领导者同步后，领导者才会进行广播阶段的工作。**广播阶段**是正常的操作模式，领导者不断提出新的客户请求，直到失败。
![][image-2]

 与Zab相比，Raft中没有明显的同步阶段：领导者通过比较每个条目的日志索引和术语值，在正常运行阶段与每个跟随者保持同步。如图2所示，缺乏明显的同步阶段简化了Raft的算法状态，但在实践中可能会导致更长的恢复时间。

# 引用：
[https://cse.buffalo.edu/tech-reports/2016-02.orig.pdf][1]
[https://static.googleusercontent.com/media/research.google.com/zh-CN//archive/paxos\_made\_live.pdf][2]

[1]:	https://cse.buffalo.edu/tech-reports/2016-02.orig.pdf
[2]:	https://static.googleusercontent.com/media/research.google.com/zh-CN//archive/paxos_made_live.pdf

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gsak007whjj30ns0ba0ts.jpg
[image-2]:	https://tva1.sinaimg.cn/large/008i3skNly1gsalq1b9m1j30mu0ay0wr.jpg