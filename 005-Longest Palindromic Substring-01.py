## Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
## 
## Example 1:
## 
## Input: "babad"
## Output: "bab"
## Note: "aba" is also a valid answer.
## Example 2:
## 
## Input: "cbbd"
## Output: "bb"

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## 设定一个函数S2W，用来两边遍历，对于偶数字符串和奇数字符串都适用，只要s[left] == s[right]，而没有明确规定left和right需要相等
        def S2W(s,left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]      
            ##返回复核条件的范围，记得需要left+1。这和序列的索引筛选有关系。
            ##例如s='crtlevelabcde',则s[0]='c',s[2:8]='tlevel',此时需要left+1变成s[3:8]，输出的才是s[3:8]='level'。需要注意

        ## 设定一个空字符串来存储遍历出来的数值，这里应该可以优化掉
        ku = ''

        ##直接进行长度判断，然后获得两个遍历结果s1和s2，分别是奇数和偶数情况下的结果
        ##比较两个结果的长度，并且把长的那个座位返回值输出。
        for i in range(len(s)):
            ##查询奇数位的字符串，此时left=right=i
            s1 = S2W(s,i,i)
            if len(s1) > len(ku): 
                ku = s1     ##将空字符串ku更新为结果——奇数位最大回文串
            ##查询偶数位的字符串，此时left=i,right=i+1
            s2 = S2W(s,i, i + 1)
            if len(s2) > len(ku): 
                ku = s2     #如果条件符合，即偶数位最大回文串大于奇数位最大回文串，则再次更新ku
        ##输出最后的结果ku
        return ku
    
        ##这种遍历算法感觉不适合使用python，本结论差不多要950ms这样，有机会再学习一下其他语言的写法。
