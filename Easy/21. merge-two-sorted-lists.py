# 21. Merge Two Sorted Lists https://leetcode.com/problems/merge-two-sorted-lists/
# Runtime: 18 ms
# Memory Usage: 13.28 MB
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        else:
            if list2.val < list1.val:
                head = list2
                tmp1 = list1
                tmp2 = list2.next
            else:
                head = list1
                tmp1 = list1.next
                tmp2 = list2
            tmp = head
            while True:
                if tmp1 == None:
                    tmp.next = tmp2
                    return head
                if tmp2 == None:
                    tmp.next = tmp1
                    return head
                else:
                    if tmp2.val < tmp1.val:
                        tmp.next = tmp2
                        tmp2 = tmp2.next
                    else:
                        tmp.next = tmp1
                        tmp1 = tmp1.next
                    tmp = tmp.next
