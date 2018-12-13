## The count-and-say sequence is the sequence of integers with the first five terms as following:
## 
## 1.     1
## 2.     11
## 3.     21
## 4.     1211
## 5.     111221
## 1 is read off as "one 1" or 11.
## 11 is read off as "two 1s" or 21.
## 21 is read off as "one 2, then one 1" or 1211.
## 
## Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
## 
## Note: Each term of the sequence of integers will be represented as a string.
## 
##  
## 
## Example 1:
## 
## Input: 1
## Output: "1"
## Example 2:
## 
## Input: 4
## Output: "1211"


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = '1'        
        for i in range(2, n + 1):
            char,n,k = [],string[0],0
            for c in string:
                if c == n:
                    k += 1
                else:
                    char.append(str(k))
                    char.append(n)
                    k,n = 1,c
            char.append(str(k))
            char.append(n)
            string = ''.join(char)
        return string