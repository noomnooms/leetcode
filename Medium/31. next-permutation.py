# 31. Next Permutation https://leetcode.com/problems/next-permutation
# Runtime: 24 ms
# Memory Usage: 13.2 MB
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = None
        i = len(nums)-1
        while i>=0:
            if i-1>=0 and nums[i]>nums[i-1]:
                index = i-1
                break
            i-=1
        if index != None:
            ans = nums[:index]
            tmp = index+1
            for i in range(index+2, len(nums)):
                if nums[i]>nums[index] and nums[i]<nums[tmp]:
                    tmp = i
            ans.append(nums[tmp])

            right = nums[index:tmp] + nums[tmp+1:]
            right.sort()
            ans += right
            
            for i in range(len(nums)):
                nums[i] = ans[i]

        else: 
            nums.sort()
        
