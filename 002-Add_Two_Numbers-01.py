# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


## 链表翻转
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:      ## 边界条件设定
            return l2
        elif l2 is None:
            return l1
        else:
            temp = 0
            bk = ListNode(0)
            bk_Last = bk
            while(l1 or l2):
                sum = 0
                if(l1):
                    sum = l1.val
                    l1=l1.next
                if(l2):
                    sum += l2.val
                    l2=l2.next
                sum += temp
                bk_Last.next = ListNode(sum%10) ## 递归求余
                bk_Last = bk_Last.next  
                temp = (sum >= 10)
            if(temp):
                bk_Last.next = ListNode(1)
            bk_Last = bk.next
            del bk
            return bk_Last
