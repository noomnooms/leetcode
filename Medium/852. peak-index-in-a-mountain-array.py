# 852. Peak Index in a Mountain Array https://leetcode.com/problems/peak-index-in-a-mountain-array
# Runtime: 466 ms
# Memory Usage: 31.90 MB
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return i-1
