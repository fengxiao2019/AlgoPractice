20210808 - LC 120 三角形最小路径和
> 给定一个三角形 triangle ，找出自顶向下的最小路径和。

> 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
> ![][image-1]
# 解法1 递归解法
通过定义全局变量的方式
```python
var ans = math.MaxInt32
func minimumTotal(triangle [][]int) int {
    // memory := map[Key]int {}
    ans = math.MaxInt32
    dfs(0, 0, triangle, 0)
    return ans
}
/*全局变量的*/
func dfs(x int, y int, triangle [][]int, sum int) {
    if x >= len(triangle) {
        if sum < ans {
            ans = sum
        }
        return
    }
    dfs(x + 1, y, triangle, sum + triangle[x][y])
    dfs(x + 1, y + 1, triangle, sum + triangle[x][y])
}
```
# 解法2 分治法
```python

func minimumTotal(triangle [][]int) int {
    return dfs(0, 0, triangle)
}

/* 记忆化搜索 解决重复计算的问题 */
func dfs(x int, y int, triangle [][]int) int {
    if x >= len(triangle) {
        return 0
    }
    left := dfs(x + 1, y, triangle)
    right := dfs(x + 1, y + 1, triangle)
    // return min_func(left, right)
    return min_func(left, right) + triangle[x][y] 
}

func min_func(x int, y int) int {
    if x > y {
        return y
    } else {
        return x
    }
}
```

# 解法3  利用记忆化-递归的解法
```python
type Key struct {
    X, Y int
}
var memory = map[Key]int {}
func minimumTotal(triangle [][]int) int {
    memory := map[Key]int {}
    return dfs(0, 0, triangle, memory)
}

/* 记忆化搜索 解决重复计算的问题 */
func dfs(x int, y int, triangle [][]int, memory map[Key]int) int {
    if x >= len(triangle) {
        return 0
    }

    if val, ok := memory[Key{x, y}]; ok {
        return val
    }

    left := dfs(x + 1, y, triangle, memory)
    right := dfs(x + 1, y + 1, triangle, memory)
    // return min_func(left, right)
    memory[Key{x, y}] = min_func(left, right) + triangle[x][y] 
    return memory[Key{x, y}]
}


func min_func(x int, y int) int {
    if x > y {
        return y
    } else {
        return x
    }
}
```
# 解法4 自低向上的dp 解法1 
```python
func minimumTotal(triangle [][]int) int {
    n := len(triangle)
    
    dp := make([][]int, n)
    for i := 0;i < n; i++ {
        dp[i] = make([]int, n)
    }

    //fmt.Printf("%v, %v %v", n, triangle[n-1], dp)
    // 初始化

    for i, v := range triangle[n-1] {
        
        dp[n-1][i] = v
    }
    for i := n - 2; i >= 0; i-- {
        for j, v := range triangle[i] {
            dp[i][j] = min_func(dp[i + 1][j], dp[i+1][j+1]) + v
        }
    }
    return dp[0][0]
}

func min_func(x int, y int) int {
    if x > y {
        return y
    } else {
        return x
    }
}
```
 另一种解法: 可以多出来一层，多出来的一层全部都是0
这样就不用初始化dp最后一层的值了，因为最后一层全是0
```python
func minimumTotal(triangle [][]int) int {
    n := len(triangle)
    
    dp := make([][]int, n + 1)
    // 声明二维数组
    for i := 0;i < n + 1; i++ {
        dp[i] = make([]int, n + 1)
    }

    // 从最底层开始向上计算
    for i := n - 1; i >= 0; i-- {
        for j, v := range triangle[i] {
            dp[i][j] = min_func(dp[i + 1][j], dp[i+1][j+1]) + v
        }
    }
    return dp[0][0]

}
```

# 解法5 自底向上的dp 解法优化
在解法4 中，当前层只和下一层有关系，所以，可以将二维数组降低成一维数组。
从左往右滚动更新数组。

```python
func minimumTotal(triangle [][]int) int {
    n := len(triangle)
    dp := triangle[n-1]

    //fmt.Printf("%v, %v %v", n, triangle[n-1], dp)
    // 初始化
    for i := n - 2; i >= 0; i-- {
        for j, v := range triangle[i] {
            dp[j] = min_func(dp[j + 1], dp[j]) + v
        }
    }
    return dp[0]
}
```

```python
func minimumTotal(triangle [][]int) int {
    n := len(triangle) + 1
    dp := make([]int, n)

    //fmt.Printf("%v, %v %v", n, triangle[n-1], dp)
    // 初始化
    for i := n - 2; i >= 0; i-- {
        for j, v := range triangle[i] {
            dp[j] = min_func(dp[j + 1], dp[j]) + v
        }
    }
    return dp[0]
}
```
# 解法6 自顶向下的dp解法

# 解法7 自顶向下的dp 解法优化

[image-1]:	https://tva1.sinaimg.cn/large/008i3skNly1gt9rfgvcxij30ue0hqq3w.jpg