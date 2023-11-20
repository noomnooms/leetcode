# 137. Single Number II https://leetcode.com/problems/single-number-ii/
# Runtime: 36 ms
# Memory Usage: 15.86 MB
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {}
        for i in nums:
            try: 
                cnt[i] += 1
                if cnt[i] == 3: del cnt[i]
            except: cnt[i] = 1
        return cnt.keys()[0]