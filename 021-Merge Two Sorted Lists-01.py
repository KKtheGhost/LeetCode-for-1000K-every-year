## Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
## 
## Example:
## 
## Input: 1->2->4, 1->3->4
## Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = cur = ListNode(0)                    ##做一个haed和cur的bond
        while l1 or l2:                             ##分别同时遍历两个链表
            v1 = l1.val if l1 else float('inf')     ##首先判断l1然后判断无限大，最后v1取l1的当前值
            v2 = l2.val if l2 else float('inf')     ##首先判断l2然后判断无限大，最后v2取l2的当前值
            if v1 <= v2:                            ##如果v1比较小，链表cur.next指向l1
                cur.next = l1                           
                l1, cur = l1.next, cur.next         ##l1指向下一位，cur指向下一位
            else:                                   ##如果v2比较小，链表cur.next指向l2
                cur.next = l2
                l2, cur = l2.next, cur.next         ##l2指向下一位，cur指向下一位
        return head.next                            ##最后返回head，不能返回cur是因为cur每次都清空
    
##self.val = x         当前的节点值
##self.next = None     下一个节点值