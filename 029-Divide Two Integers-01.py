## Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
## 
## Return the quotient after dividing dividend by divisor.
## 
## The integer division should truncate toward zero.
## 
## Example 1:
## 
## Input: dividend = 10, divisor = 3
## Output: 3
## Example 2:
## 
## Input: dividend = 7, divisor = -3
## Output: -2
## Note:
## 
## Both dividend and divisor will be 32-bit signed integers.
## The divisor will never be 0.
## Assume we are dealing with an environment which could only store integers within 
## the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
## assume that your function returns 231 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = 0
        if dividend == 0:
            return 0
        if dividend*divisor > 0:
            res = dividend//divisor
        else:
            if (dividend//divisor)*divisor == dividend:
                res = dividend//divisor
            else:
                res = (dividend//divisor)+1
        if res > 2147483647:
            return 2147483647
        elif res < -2147483648:
            return -2147483648
        else:
            return res