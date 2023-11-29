# 191. Number of 1 Bits https://leetcode.com/problems/number-of-1-bits/
# Runtime: 38 ms
# Memory Usage: 16.12 MB
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
