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
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
    
## stack通常的操作：
## Stack() 建立一个空的栈对象
## push() 把一个元素添加到栈的最顶层
## pop() 删除栈最顶层的元素，并返回这个元素
## peek() 返回最顶层的元素，并不删除它
## isEmpty() 判断栈是否为空
## size() 返回栈中元素的个数   