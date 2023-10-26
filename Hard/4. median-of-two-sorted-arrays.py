# 4. Median of Two Sorted Arrays https://leetcode.com/problems/median-of-two-sorted-arrays/
# Runtime: 88 ms
# Memory Usage: 14.2 MB
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)

        if len(nums1) % 2 == 1:
            return float(nums1[int(len(nums1)/2)])
        else:
            v1 = float(nums1[int(len(nums1)/2)-1])
            v2 = float(nums1[int(len(nums1)/2)])
            return float((v1+v2)/2)
