# 9. Palindrome Number https://leetcode.com/problems/palindrome-number/
# Runtime: 52 ms
# Memory Usage: 14.2 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False