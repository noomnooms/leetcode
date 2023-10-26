# 11. Container With Most Water https://leetcode.com/problems/container-with-most-water/
# Runtime: 772 ms
# Memory Usage: 27.4 MB
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        max_size = 0
        while right > left:
            max_size = max(max_size, (right-left) *
                           min(height[right], height[left]))

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_size
