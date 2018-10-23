##Implement atoi which converts a string to an integer.
##
##The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
##
##The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
##
##If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
##
##If no valid conversion could be performed, a zero value is returned.
##
##Note:
##
##Only the space character ' ' is considered as whitespace character.
##Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
##Example 1:
##
##Input: "42"
##Output: 42
##Example 2:
##
##Input: "   -42"
##Output: -42
##Explanation: The first non-whitespace character is '-', which is the minus sign.
##             Then take as many numerical digits as possible, which gets 42.
##Example 3:
##
##Input: "4193 with words"
##Output: 4193
##Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
##Example 4:
##
##Input: "words and 987"
##Output: 0
##Explanation: The first non-whitespace character is 'w', which is not a numerical 
##             digit or a +/- sign. Therefore no valid conversion could be performed.
##Example 5:
##
##Input: "-91283472332"
##Output: -2147483648
##Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
##             Thefore INT_MIN (−2^31) is returned.

##特殊情况和边界条件很多，所以比较难度巨大。
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        index,signal,max,min,allsum = 0,1,2147483647,-2147483648,0              ##设定索引，上下边界，正负值配置，以及求和
        if str == '':                                                           ##情况1：字符串为空
            return 0
        while index < len(str) and str[index].isspace():                        ##循环，跳过字符串中的空格部分
            index += 1
        if index < len(str) and str[index] == '-':                              ##检查字符串中的第一个‘-’，从而设定输出结果的正负值
            signal = -1                                                         ##因为The first non-whitespace character is '-', which is the minus sign
        if index < len(str) and (str[index] == '+' or str[index] == '-'):       ##检查之后的‘-’和‘+’，直接跳过
            index += 1

        ##上面部分处理了空字符串、正负值、多于正负字符跳过这几个特殊情况，下面部分是正式的字符处理遍历循环。
        while index < len(str) and str[index].isdigit():                        ##开始检测最大值和最小值的边界情况，从左数第一个数字开始进行循环累加，这个条件还导致必须是连续数字才能进行循环。
            digit = int(str[index])                                             ##如果遇到非数字会导致循环跳出。
            if max/10 >= allsum:                                                ##如果总和小于’最大值/10‘的情况下，每次循环后对总和*10，为下一个数位腾个位空间
                allsum *= 10
            else:
                if signal == 1:                                                 ##如果是正数，而且此时总和已经大于’最大值/10‘，意味着再进行一次循环后肯定超过范围了，直接范围最大值
                    return max
                else:                                                           ##如果是负数，理由同上，范围最小值
                    return min
            if max - digit >= allsum:                                           ##如果（最大值-进入循环的数位）大于当前的总和，则总和=原总和+数位（可以保证不越界）
                allsum += digit         
            else:                                                               ##如果会大于，意味着下次相加以后发生越界，直接输出最大值
                if signal == 1:
                    return max
                else:                                                           ##同上，碰到下边界输出最小值
                    return min                  
            index += 1                                                          ##索引+1继续循环
        return signal*allsum                                                    ##如果都没有发生越界的情况下跳出了循环直接输出结果，正负值*总和即可