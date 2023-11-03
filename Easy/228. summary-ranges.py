# 228. Summary Ranges https://leetcode.com/problems/summary-ranges/
# Runtime: 7 ms
# Memory Usage: 13.4 MB
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        ans = [[nums[0], nums[0]]]
        for i in nums:
            if i-(ans[-1][1]) > 1:
                ans.append([i, i])
            else:
                ans[-1][1] = i
        return ["{}->{}".format(i[0], i[1]) if i[0] != i[1] else "{}".format(i[0]) for i in ans]
