## Implement strStr().
## 
## Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
## 
## Example 1:
## 
## Input: haystack = "hello", needle = "ll"
## Output: 2
## Example 2:
## 
## Input: haystack = "aaaaa", needle = "bba"
## Output: -1
## Clarification:
## 
## What should we return when needle is an empty string? This is a great question to ask during an interview.
## 
## For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:          ## needle为""，返回0
            return 0
        for i in range(len(haystack) - len(needle) + 1):        ## 确定i的遍历范围
            if haystack[i:(i+len(needle))] == needle:           ## 确定needle出现的判定条件
                return i                                        ## 返回i
        return -1                                               ## 无匹配，返回-1