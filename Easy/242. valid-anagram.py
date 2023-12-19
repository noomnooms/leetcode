# 242. Valid Anagram https://leetcode.com/problems/valid-anagram
# Runtime: 57 ms
# Memory Usage: 17.02 MB
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))
