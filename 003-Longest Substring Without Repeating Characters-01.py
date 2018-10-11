class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={}
        count=0
        first=-1
        for i in range(len(s)):
            if s[i] in a and a[s[i]]>first:
                first=a[s[i]]
            a[s[i]]=i
            count=max(count,(i-first))
        return count