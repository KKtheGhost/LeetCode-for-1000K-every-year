## Given a string, find the length of the longest substring without repeating characters.
## 
## Example 1:
## 
## Input: "abcabcbb"
## Output: 3 
## Explanation: The answer is "abc", with the length of 3. 
## Example 2:
## 
## Input: "bbbbb"
## Output: 1
## Explanation: The answer is "b", with the length of 1.
## Example 3:
## 
## Input: "pwwkew"
## Output: 3
## Explanation: The answer is "wke", with the length of 3. 
##              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':                     ##特殊情况，s为空字符串，返回0
            return 0
        b,i = '',0                      ##初始化输出字符串b和遍历起始索引i
        while i < len(s):               ##限定i的范围
            a,j = '',i                  ##初始化中转字符串a和遍历索引j
            while j < len(s):           ##开始从索引i处开始往后遍历
                if s[j] not in a:       ##把最长连续无重复字符串导入a中
                    a = a + s[j]
                    j += 1
                else:                   ##出现重复字符则跳出本循环
                    break
            if len(a) > len(b):         ##比较a和输出字符串b，如果a比较长则更新b
                b = a
            else:
                b =b
            i += 1
        return len(b)                   ##最后输出字符串b的长度