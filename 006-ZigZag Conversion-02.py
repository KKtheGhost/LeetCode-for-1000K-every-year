##The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
##
##P   A   H   N
##A P L S I I G
##Y   I   R
##And then read line by line: "PAHNAPLSIIGYIR"
##
##Write the code that will take a string and make this conversion given a number of rows:
##
##string convert(string s, int numRows);
##Example 1:
##
##Input: s = "PAYPALISHIRING", numRows = 3
##Output: "PAHNAPLSIIGYIR"
##Example 2:
##
##Input: s = "PAYPALISHIRING", numRows = 4
##Output: "PINALSIGYAHRPI"
##Explanation:
##
##P     I    N
##A   L S  I G
##Y A   H R
##P     I

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ##如果行数小于0，那就是顺序，也就是源字符串。如果行数大于字符长度，则其实就是正常书写，也就是原字符串。
        if numRows <= 1 or numRows >= len(s):
            return s
        
        ##一个比较数学化的解法
        arr = [''] * numRows                            ##创建一个空的，个数为行数的，字符串序列
        for i in xrange(len(s)):                        ##遍历所有i个字符
            yu = i % (2 * numRows - 2)                  ##第一行的每个字符的i都是2*numRows-2的自然数倍。余数就代表第几行。
            if yu < numRows:                            ##余数小于行数，直接把对应数字丢到余数行标号的字符串中
                arr[yu] += s[i]
            else:                                       ##余数大于等于numRows且小于2*numRows-2，也就是在И的斜杠部位，特别处理
                arr[2 * numRows - 2 - yu] += s[i]
        return ''.join(arr)                             ##最后合并arr直接输出