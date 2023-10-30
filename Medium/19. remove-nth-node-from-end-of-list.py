# 19. Remove Nth Node From End of List https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Runtime: 31 ms
# Memory Usage: 16.10 MB
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        nodes = [head]
        while True:
            tmp = tmp.next
            if tmp == None:
                break
            nodes.append(tmp)

        if len(nodes)-n == 0:
            try:
                return nodes[1]
            except:
                return None

        if n == 1:
            next = None
        else:
            next = nodes[len(nodes)-n+1]

        nodes[len(nodes)-n-1].next = next
        return head
