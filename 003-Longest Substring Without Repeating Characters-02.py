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

class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        count=1
        temp=1
        sub=""+s[0]
        f=0
        for i in range(1,len(s)):
            if sub.find(s[i])==-1:
                sub=sub+s[i]
                temp+=1
            else:
                f=sub.find(s[i])+1
                sub=sub[f::]+s[i]
                temp=temp-f+1
            if temp>count:
                count=temp
        return count 