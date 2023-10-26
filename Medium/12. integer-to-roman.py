# 12. Integer to Roman https://leetcode.com/problems/integer-to-roman/
# Runtime: 52 ms
# Memory Usage: 14.3 MB
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''

        thousand = int(num / 1000)
        ans += 'M'*thousand
        num %= 1000

        hundred = int(num / 100)
        if hundred == 9:
            ans += 'CM'
        elif hundred in range(5, 9):
            ans += 'D' + 'C'*(hundred-5)
        elif hundred == 4:
            ans += 'CD'
        elif hundred in range(1, 4):
            ans += 'C'*hundred
        num %= 100

        tens = int(num / 10)
        if tens == 9:
            ans += 'XC'
        elif tens in range(5, 9):
            ans += 'L' + 'X'*(tens-5)
        elif tens == 4:
            ans += 'XL'
        elif tens in range(1, 4):
            ans += 'X'*tens
        num %= 10

        if num == 9:
            ans += 'IX'
        elif num in range(5, 9):
            ans += 'V' + 'I'*(num-5)
        elif num == 4:
            ans += 'IV'
        elif num in range(1, 4):
            ans += 'I'*num
        return ans
