# 17. Letter Combinations of a Phone Number https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Runtime: 44 ms
# Memory Usage: 16.17 MB
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        size = len(digits)
        ans = map[digits[0]]
        for i in range(1, size):
            tmp = ans*len(map[digits[i]])
            cnt = 0
            for j in range(len(tmp)):
                tmp[j] += map[digits[i]][cnt]
                if (j+1) % len(ans) == 0:
                    cnt += 1
            ans = tmp

        return ans
