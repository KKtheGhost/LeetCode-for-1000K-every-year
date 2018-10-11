class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,sub = 0,''
        for c in s:
            if c in sub: sub = sub.split(c)[-1]
            sub += c
            if len(sub)>l: l = len(sub)
        return(l) 