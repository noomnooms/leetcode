# 15. 3sum https://leetcode.com/problems/3sum/
# Runtime: 688 ms
# Memory Usage: 17.3 MB
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        ans = []
        
        for i  in range(len(nums)-2):
            if nums[i] > 0: # udh nyentuh positif
                break
            if i>0 and nums[i] == nums[i-1]: # double numbers
                continue
                
            j = i+1 # dari i+1
            k = len(nums)-1 # dr blakang
            while j<k:
                s = nums[i] + nums[j] + nums [k]
                if s>0: k-=1 # k kegedean
                elif s<0: j += 1 # j kekecilan
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j+=1
                    k-=1
        return ans