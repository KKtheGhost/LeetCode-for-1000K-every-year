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
        ##边界条件：如果行数小于0，那就是顺序，也就是源字符串。如果行数大于字符长度，则其实就是正常书写，也就是原字符串。
        if numRows <= 1 or numRows >= len(s):       
            return s
        
        ##创建一个元素数量为行数的字符串列表，用来填充。
        ##给原始字符串的每个字符标注行数，其实就是一个123...(n-1)n(n-1)...32123...的一个序列
        #  也就是每个字符的行数和前一个字符的行数一定是+1或者-1的关系。
        ##这样我们通过arr[line]，然后把所有arr[1],arr[2],arr[3]...arr[n-1],arr[n]
        #  用join函数串成一个字符串，就好了。

        arr = [''] * numRows                ##创建一个长度为行数的空字符串列表
        line, step = 0, -1                  ##预设行数为0(因为join操作的时候从索引0开始排列)，步长为-1
        for c in s:                         ##通过循环来生成arr这个字符串列表。
            arr[line] += c                  ##向arr[line]中添加s的成员。
            if line % (numRows-1) == 0:     ##因为从line = 0开始，所以第N行的时候应该可以整除N-1.
                step = - step               ##当line可以整除n-1的时候，改变行数变化方向，所以step = -step
            line += step                    ##line根据步长变化，继续添加。
        ##在上面一个循环里，假如s = "PAYPALISHIRING",numRow=4的话，
        #  循环的产生顺序也就是arr[0] == 'P',然后arr[1] == 'A',然后arrp[2] == 'Y'
        ##然后arr[3]='P',然后arr[2]='YA',arr[1]='AL'...这样的顺序进行不停地添加，最后得到如下四个arr
        ##arr[0]='PIN',arr[1]='ALSIG',arr[2]='YAHR',arr[3]='PI'
        
        ##最后通过join函数组合成为"PINALSIGYAHRPI"，也就是把arr={'PIN','ALSIG','YAHR','PI'}合并成一个字符串
        return ''.join(arr)
