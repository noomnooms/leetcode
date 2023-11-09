# 27. Remove Element https://leetcode.com/problems/remove-element/
# Runtime: 20 ms
# Memory Usage: 13.25 MB
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt = 0
        ans = []
        for i in nums: 
            if i !=  val: ans.append(i)
        for i in range(len(ans)):
            nums[i]=ans[i]
        return len(ans)
