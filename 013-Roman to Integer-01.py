## Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
## 
## Symbol       Value
## I             1
## V             5
## X             10
## L             50
## C             100
## D             500
## M             1000
## For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
## 
## Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
## 
## I can be placed before V (5) and X (10) to make 4 and 9. 
## X can be placed before L (50) and C (100) to make 40 and 90. 
## C can be placed before D (500) and M (1000) to make 400 and 900.
## Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
## 
## Example 1:
## 
## Input: "III"
## Output: 3
## Example 2:
## 
## Input: "IV"
## Output: 4
## Example 3:
## 
## Input: "IX"
## Output: 9
## Example 4:
## 
## Input: "LVIII"
## Output: 58
## Explanation: L = 50, V= 5, III = 3.
## Example 5:
## 
## Input: "MCMXCIV"
## Output: 1994
## Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

## 本题的关键还是去逐个处理s中的字符，也就是从左往右遍历，老题型了
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ##建立罗马表和数字的对应表，这里不用字典因为字典基于哈希值，是无序的。
        d1 = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        d2 = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i,j,num = 0,0,0                     ##初始化两个索引和总和num
        while i < len(d1):                  ##针对s的索引进行字符串遍历
            if s[j:j+1] == d1[i]:           ##因为罗马文单位对应两种字符串长度，所以条件判断
                num += d2[i]                ##先进行一位罗马文判断，再进行两位罗马文判断
                j += 1
            elif s[j:j+2] == d1[i]:
                num += d2[i]
                j += 2                      ##注意两位罗马文判断的话s的索引要进两位
            else:
                i += 1                      ##如果无结果只需要d1的索引+1继续遍历即可
                num = num
        return num                          ##最后输出相加后的num
