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

        ## 设定一个空字符串来存储遍历出来的数值，这里应该可以优化掉
        ku = ''

        ##直接进行长度判断，然后获得两个遍历结果s1和s2，分别是奇数和偶数情况下的结果
        ##比较两个结果的长度，并且把长的那个座位返回值输出。
        for i in range(len(s)):
            s1 = S2W(s,i,i)
            if len(s1) > len(ku): 
                ku = s1
            s2 = S2W(s,i, i + 1)
            if len(s2) > len(ku): 
                ku = s2

        return ku
    
##这种遍历算法感觉不适合使用python，本结论差不多要950ms这样，有机会再学习一下其他语言的写法。
