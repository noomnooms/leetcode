# 16. 3Sum Closest https://leetcode.com/problems/3sum-closest/
# Runtime: 112 ms
# Memory Usage: 14.3 MB
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        ans = 0

        for i in range(len(nums)-2):
            j = i+1  # dari i+1
            k = len(nums)-1  # dr blakang
            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if abs(target-s) < abs(diff):
                    diff = target-s
                if s < target:
                    j += 1
                else:
                    k -= 1
            if diff == 0:
                break
        return target - diff
