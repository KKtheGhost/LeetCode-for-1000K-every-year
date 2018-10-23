##Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
##
##Example 1:
##
##Input: 121
##Output: true
##Example 2:
##
##Input: -121
##Output: false
##Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
##Example 3:
##
##Input: 10
##Output: false
##Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

##本方法并不完全符合要求，因为需要把int转化为str。
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)   ##天才方法，直接分片-1步长遍历相等。