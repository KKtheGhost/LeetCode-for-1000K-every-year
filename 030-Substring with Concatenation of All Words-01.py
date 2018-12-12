## You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
## 
## Example 1:
## 
## Input:
##   s = "barfoothefoobarman",
##   words = ["foo","bar"]
## Output: [0,9]
## Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
## The output order does not matter, returning [9,0] is fine too.
## Example 2:
## 
## Input:
##   s = "wordgoodstudentgoodword",
##   words = ["word","student"]
## Output: []

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:                                       ## words空值
            return []
        L = len(words[0])                                   ## words元素等长，所以长度为L
        res = []                                            ## 输出用res
        for left in range(L):                               ## 左侧索引 left
            N = collections.Counter(words)                  ## 设定计数器Counter
            for right in range(left + L, len(s) + 1, L):    ## 右侧索引 right，步长L
                word = s[right - L: right]                  ## 从右侧开始排word
                N[word] -= 1                                
                while N[word] < 0:                          
                    N[s[left:left + L]] += 1
                    left += L
                if left + L * len(words) == right:
                    res.append(left)
        return res