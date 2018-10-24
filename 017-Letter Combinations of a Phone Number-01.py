## Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
## 
## A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
## 
## 【1】【2】【3】
## 【4】【5】【6】
## 【7】【8】【9】
## 【*】【0】【#】
## 
## Example:
## 
## Input: "23"
## Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
## Note:
## 
## Although the above answer is in lexicographical order, your answer could be in any order you want.

##其实就是一个多重循环，很简单，每多一位数字，对于输出序列的每个元素就重新做一次循环，并且更新输出循环
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':                ##如果数字字符串为空，返回空值
            return []
        letters = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        ##创建一个字典，用来跑循环调用，这个过程中无序也没事，所以可以用字典。
        elems = ['']                    ##创建一个输出用的列表
        for num in digits:              ##第一层循环，对于任何一个digits钟的字符num
            elemsN = []                 ##创建二层循环和三层循环中用的中转字符串elemsN
            for elem in elems:          ##对于elems中的元素elem
                for letter in letters[int(num)]:        ##循环所有letters[int(num)]中的字符
                    elemsN.append(elem+letter)          ##全部添加到elemsN中，第一次循环elems是空列表，所以只会传入第一个int(num)对应的几个字符
                                                        ##之后就是指数扩张了
            elems = elemsN                              ##每个num下被遍历完后更新elems
        return elems                                    ##最后输出elems