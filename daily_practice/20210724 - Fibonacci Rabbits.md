**问题描述**
- 第一个月的月初有一对刚诞生的兔子
- 第二个月之后他们可以生育
- 每月每对可以生育的兔子都会剩下一对新兔子
- 兔子永远不死去

**用图形绘制出生育的规律**
![][image-1]

假设在第n月有a对兔子
在第n+1月有b对兔子
那么，在第n+2月就会有a+b对兔子，其中b对兔子是存量，第n月的a对兔子在第n+2月都可以生育，会生成a对新兔子
这就是为什么斐波那契数列也被称之为“兔子队列”的原因。
**斐波那契数列算法**
**算法1-递归解法**
```python
def fib(n: int) -> int:
	if n <= 1: return n 
	return fib(n - 1) + fib(n - 2)
```
**算法2-记忆化递归**
```python
def fib(n: int) -> int:
	mem = [0] * (n + 1)
	def dfs(n: int) -> int:
		if n <= 1: return 1
		if mem[n]: return mem[n]
		mem[n] = dfs(n-1) + dfs(n-2)
		return mem[n]
	dfs(n)
	return mem[-1]	
```
**算法3-dp解法**
```python
def fib(n: int) -> int:
	mem = [0] * (n + 1)
	mem[0], mem[1] = 1, 1
	for i in range(2, n + 1):
		mem[i] = mem[i-1] + mem[i-2]
	return mem[-1]

```
**算法4-dp优化解法**
```python
def fib(n: int) -> int:
	if n <= 1: return n
	first, second = 1, 1
	for n in range(2, n + 1):
		cur = first + second
		first = second
		second = cur
	return cur
```


[image-1]:	https://tva1.sinaimg.cn/large/008i3skNgy1gsrufdfra5j317m0lgmy8.jpg