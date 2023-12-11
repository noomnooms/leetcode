# 1287. Element Appearing More Than 25% In Sorted Array https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
# Runtime: 62 ms
# Memory Usage: 14.25 MB
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        qrtr = len(arr)/4
        cnt = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                cnt = 1
            else:
                cnt += 1

            if cnt > qrtr:
                return arr[i]
        return arr[0]
