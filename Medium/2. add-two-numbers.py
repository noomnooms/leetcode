# 2. Add Two Numbers https://leetcode.com/problems/add-two-numbers/
# Runtime: 76 ms
# Memory Usage: 14.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while p != None or q != None:
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            summ = carry + x + y
            print(summ)
            carry = int(summ / 10)
            curr.next = ListNode(summ % 10)
            curr = curr.next
            
            if (p != None):
                p = p.next
            if (q != None):
                q = q.next
        
        if carry > 0:
            curr.next = ListNode(carry%10)
        return dummy.next