# 24. Swap Nodes in Pairs https://leetcode.com/problems/swap-nodes-in-pairs/
# Runtime: 17 ms
# Memory Usage: 13.27 MB

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        linked = [[head.next, head]]
        curr = head.next.next
        while curr != None:
            if len(linked[-1]) == 2:
                linked.append([curr])
            else:
                linked[-1] = [curr, linked[-1][0]]
            curr = curr.next

        ans = linked[0][0]
        ans.next = linked[0][1]
        curr = ans.next
        curr.next = None
        for i in range(1, len(linked)):
            try:
                curr.next = linked[i][0]
                curr.next.next = linked[i][1]
                curr = curr.next.next
                curr.next = None
            except:
                pass
        return ans
