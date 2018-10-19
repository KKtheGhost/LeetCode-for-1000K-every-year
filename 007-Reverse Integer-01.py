##Given a 32-bit signed integer, reverse digits of an integer.
##
##Example 1:
##
##Input: 123
##Output: 321
##Example 2:
##
##Input: -123
##Output: -321
##Example 3:
##
##Input: 120
##Output: 21
##Note:
##Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
##For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

##此方法把x转化为str，我认为没必要，大有优化空间。
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        b,y = 0,str(abs(x))                     ##把x的绝对值转化为str便于列表化处理
        z = 1 if x >= 0 else -1                 ##添加一个用于正负数处理的值z
        for i in range(len(y)):                 ##开始遍历循环x的每一位数字
            a = (int(y[i])) * (10**(i))         ##根据数字的位数得到每一位转化后的值a
            b += a                              ##把每次循环的a累加起来获得结果的绝对值
        b2 = b * z                              ##把结果和x的正负进行统一
        ##判断输出值是否在long范围内，如果是则输出b2，如果不是则输出0
        return b2 if b2 < 2147483648 and b2 >= -2147483648 else 0
