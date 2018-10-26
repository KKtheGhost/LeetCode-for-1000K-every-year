## Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
## 
## An input string is valid if:
## 
## Open brackets must be closed by the same type of brackets.
## Open brackets must be closed in the correct order.
## Note that an empty string is also considered valid.
## 
## Example 1:
## 
## Input: "()"
## Output: true
## Example 2:
## 
## Input: "()[]{}"
## Output: true
## Example 3:
## 
## Input: "(]"
## Output: false
## Example 4:
## 
## Input: "([)]"
## Output: false
## Example 5:
## 
## Input: "{[]}"
## Output: true


## 一道入门级的栈问题
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []                                              ##建立一个空的栈
        dict = {"]":"[", "}":"{", ")":"("}                      ##创建一个字典用来存储配对关系
        for char in s:                                          ##遍历字符串中的字符
            if char in dict.values():                           ##如果char在字典的value里面，说明是一个括号组的开始
                stack.append(char)                              ##往栈中加入char
            elif char in dict.keys():                           ##如果char在字典的key中，说明是一个括号组的结尾
                if stack == [] or dict[char] != stack.pop():    ##如果此时的stack是空值，或者不匹配目前栈的最上面的字符
                    return False                                ##返回false
            else:                                               ##其他情况返回false
                return False
        return stack == []                                      ##最后判断stack是否为空值，如果是返回true
    
## stack通常的操作：
## Stack() 建立一个空的栈对象
## push() 把一个元素添加到栈的最顶层
## pop() 删除栈最顶层的元素，并返回这个元素
## peek() 返回最顶层的元素，并不删除它
## isEmpty() 判断栈是否为空
## size() 返回栈中元素的个数   