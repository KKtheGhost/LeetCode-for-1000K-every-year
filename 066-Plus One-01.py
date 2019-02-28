## Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
## 
## The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
## 
## You may assume the integer does not contain any leading zero, except the number 0 itself.
## 
## Example 1:
## 
## Input: [1,2,3]
## Output: [1,2,4]
## Explanation: The array represents the integer 123.
## Example 2:
## 
## Input: [4,3,2,1]
## Output: [4,3,2,2]
## Explanation: The array represents the integer 4321.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(map(int, str(int(''.join(map(str, digits)))+1)))

## 首先把整个list进行map函数遍历，并且通过把每一个字符转化为str的方法，配合join生成一个str，然后再转化为int进行+1计算。
## 然后反向操作日神仙，对int进行str转化，然后继续用map工具对每一位进行遍历并转化为int，然后用list方法添加到列表中。
