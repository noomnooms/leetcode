# 2090. K Radius Subarray Averages https://leetcode.com/problems/k-radius-subarray-averages/
# Runtime: 1203 ms
# Memory Usage: 33.87 MB
class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [-1 for i in nums]
        try:
            divisor = k*2+1
            total = sum([nums[i] for i in range(divisor)])

            for i in range(k, len(nums)-k):
                if i>k:
                    total -= nums[i-k-1]
                    total += nums[i+k]
                ans[i] = total//divisor
        except:
            pass
        return ans