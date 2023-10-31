# 2433. Find The Original Array of Prefix Xor https://leetcode.com/problems/find-the-original-array-of-prefix-xor
# Runtime: 601 ms
# Memory Usage: 33.16 MB
class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        return [pref[0]] + [pref[i-1] ^ pref[i] for i in range(1, len(pref))]
