260. Single Number III
给定一个整数数组nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

```python
"""
思想：利用的思想A ^ A = 0
     数组内所有元素全部异或操作完之后的结果其实就是A ^ B，假设A B是数组内只出现一次的元素
     res = A ^ B
     异或的结果，1 说明 A 和 B 对应的bit 是不同的
     这样，可以利用这个特性，我们可以找到res中的第一个为1的bit，把数组分成两组，一组是在对应bit上为1的所有的元素，另一组是对应bit上为0的所有元素。
     这样的话，就把A 和 B分到了不同的组里面，对不同的组做异或就可以得到A 和 B。
时间复杂度：O(n)
空间复杂度：O(1)
"""

def singleNumber(nums: List[int]) -> List[int]:
    xor_res = 0
    for item in nums:
        xor_res ^= item
    ####### 找到一个bit位为1的mask
    mask = 0
    for i in range(32):
        if xor_res & (1 << i):
            mask = 1 << i
            break

    ###### 也可以这么写
    mask = xor_res &(-xor_res) # 找到第一个为1bit（从高->低）
    ans = [0, 0]
    for item in nums:
        if mask & item:
            ans[0] ^= item
        else:
            ans[1] ^= item
    return ans
```
