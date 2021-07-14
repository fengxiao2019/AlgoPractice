OAuth2.0解决的问题
> 一套授权机制来应对现实中的所有场景，比如 Web 应用场景、移动 App 应用场景、官方应用场景等等，但是这些场景并不是完全相同的

**OAuth 2.0的核心** 归结两点的话，就是：生成access_token和使用access_token，受保护资源只能被允许使用`access_token`，不能被允许使用授权码。授权码仅仅是一个“中间值”。_ 
**OAuth 1.0  存在的问题：安全上的固化攻击等问题**
**OAuth 2.0授权许可机制类型**:
- 授权码许可机制
- 客户端凭据机制
- 资源拥有者凭据机制
- 隐式许可机制

**为什么需要通过授权码去换取token，而不是直接获取token？**
- code是给客户端的，不安全，时效短。(比如通过web跳转传回来，这个时候code就是暴露的。当然也有类似JS直接获取的，同样也是暴露的)
- code换取的token往往是服务端之间的通讯，是保密且比较长时间有效的。
- token是用户与授权方交互才能直接给出的，如果第三方要直接获取token，说明用户跟授权方的交互要委托给第三方。比如你的用户名密码要给到第三方，第三方再跟授权方换取token，这里就向第三方暴露了用户的机密。
**授权码许可类型的通信过程**
![][image-1] 授权码获取过程
![][image-2]token获取过程
￼

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gse90a2hufj61060kmq6o02.jpg
[image-2]:	https://tva1.sinaimg.cn/large/008i3skNly1gse99jivbij30qk0jk0x7.jpg