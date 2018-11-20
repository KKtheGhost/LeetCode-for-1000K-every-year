## Given a linked list, remove the n-th node from the end of list and return its head.
## 
## Example:
## 
## Given linked list: 1->2->3->4->5, and n = 2.
## 
## After removing the second node from the end, the linked list becomes 1->2->3->5.
## Note:
## 
## Given n will always be valid.
## 
## Follow up:
## 
## Could you do this in one pass?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        move = head
        stay = head
        for i in range(n):
            move = move.next
        if move is None:
            head = head.next
            return head
        while move.next != None:
            move = move.next
            stay = stay.next
        stay.next = stay.next.next
        return head