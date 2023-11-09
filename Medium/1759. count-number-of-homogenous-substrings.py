# 1759. Count Number of Homogenous Substrings https://leetcode.com/problems/count-number-of-homogenous-substrings
# Runtime: 94 ms
# Memory Usage: 17.15 MB
class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 1
        ans = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                ans += (cnt*(cnt+1))/2
                cnt = 1
        ans += (cnt*(cnt+1))/2
        return ans % 1000000007
