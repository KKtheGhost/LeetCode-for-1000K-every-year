## Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
## 
## For example, given n = 3, a solution set is:
## 
## [
##   "((()))",
##   "(()())",
##   "(())()",
##   "()(())",
##   "()()()"
## ]

class Solution:
    def generateParenthesis(self, n, open=0):
        """
        :type n: int
        :rtype: List[str]
        """
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)