# Roman to Integer https://leetcode.com/problems/roman-to-integer/
# Runtime: 56 ms
# Memory Usage: 14 MB
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        special = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        ans = 0
        i = 0
        while i < len(s):
            # check special
            c = s[i]
            if i < len(s)-1:
                if c+s[i+1] in special.keys():
                    ans += special[c+s[i+1]]
                    i += 2
                    continue
            ans += roman[c]
            i += 1
        return ans
