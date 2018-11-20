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

##本方法很差，因为需要把int转化为str，效率大大降低。
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        i,s = 0,1                          ##设定索引i和真假判断值s
        y = str(x)                         ##转化x为str便于处理
        if x < 0:                          ##如果x小于零直接判定为false
            return bool(0)
        else:                              ##如果x大于等于0
            l = len(str(x)) - 1            ##从x的两边开始往中间一位位的对比
            while i <= int(l):             ##设置边界范围 
                if y[i] == y[l]:           ##如果两个值相等
                    s *= 1                 ##真假判断值保持为真，索引+1
                    i += 1
                    l -= 1
                else:                      ##如果发生不等则直接判定假
                    s *= -1
                    break
            if s == 1:                     ##最后通过真假判断值来输出真假结果
                return bool(1)
            else:
                return bool(0)