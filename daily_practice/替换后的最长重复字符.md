424. 替换后的最长重复字符

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意：字符串长度 和 k 不会超过 104。
```python
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。
```

**代码**
```python
"""
ABABCE   k=2
利用双指针+hash表
l，r 同时指向下标0
|-------|
l       r
这个范围内能够构成的最大连续字符的个数位len_r_l
len_r_l = max(dup_char) + k 
可见，如果想要len_r_l 足够长，因为k是固定的，我们就需要最多次重复的字符
我们固定l，r两个指针在下标0处
r 一直前进，前进的过程中统计字符出现的次数
如果len_r_l - max(dup_char) > k:
    l 前进一位
    同时对l所在下标的字符进行减一操作

len_r_l 在前进过程中的最大值就是所需结果
时间复杂度：O(n)
空间复杂度：O(n)
"""

def characterReplacement(s: str, k: int) -> int:
    if not s: return 0
    #if len(s) <= k: return min(len(s)m, k)
    l, r = 0, 0
    max_dup_len = 0
    hash_map = collections.Counter()
    res = 1
    while r < len(s):
        hash_map[s[r]] += 1
        max_dup_len = max(max_dup_len, hash_map[s[r]])
        
        len_r_l = r - l + 1
        if len_r_l - max_dup_len > k:
            hash_map[s[l]] -= 1
            l += 1
        
        r += 1
        res = max(res, r - l)
    return res
```
