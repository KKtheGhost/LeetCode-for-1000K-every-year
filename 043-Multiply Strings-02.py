 ## Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
 ## 
 ## Example 1:
 ## 
 ## Input: num1 = "2", num2 = "3"
 ## Output: "6"
 ## Example 2:
 ## 
 ## Input: num1 = "123", num2 = "456"
 ## Output: "56088"
 ## Note:
 ## 
 ## The length of both num1 and num2 is < 110.
 ## Both num1 and num2 contain only digits 0-9.
 ## Both num1 and num2 do not contain any leading zero, except the number 0 itself.
 ## You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0': return '0'
        a, b, len_a, len_b = [ord(i) - 48 for i in num1[::-1]], [ord(j) - 48 for j in num2[::-1]], len(num1), len(num2)
        res = [0] * (len_a + len_b)
        for i in xrange(len_a):
            for j in xrange(len_b):
                res[i + j] += a[i] * b[j]
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10
        return ''.join([chr(48 + x) for x in res])[::-1].lstrip('0')