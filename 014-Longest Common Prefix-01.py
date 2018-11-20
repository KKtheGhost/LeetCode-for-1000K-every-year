## Write a function to find the longest common prefix string amongst an array of strings.
## 注意是最长前缀，所以不是很麻烦的最长共有字符串问题
## If there is no common prefix, return an empty string "".
## 
## Example 1:
## 
## Input: ["flower","flow","flight"]
## Output: "fl"
## Example 2:
## 
## Input: ["dog","racecar","car"]
## Output: ""
## Explanation: There is no common prefix among the input strings.
## Note:
## 
## All given inputs are in lowercase letters a-z.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """ 
        if not strs:
            return ''
        a = ''
        for i in range(0,len(strs[0])):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or (strs[j])[i] != (strs[0])[i]:
                    return a
            a += (strs[0])[i]
        return a