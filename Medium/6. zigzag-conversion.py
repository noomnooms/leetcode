#  Zigzag Conversion https://leetcode.com/problems/zigzag-conversion/
# Runtime: 64 ms
# Memory Usage: 14.6 MB
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_list = {i: '' for i in range(numRows)}

        while True:
            shouldbreak = False
            for i in range(numRows):
                row_list[i] += s[0]
                s = s[1:]

                if len(s) == 0:
                    shouldbreak = True
                    break

            if shouldbreak:
                break

            for i in range(numRows-2, 0, -1):
                row_list[i] += s[0]
                s = s[1:]

                if len(s) == 0:
                    shouldbreak = True
                    break

            if shouldbreak:
                break

        ans = ''
        for i in row_list.values():
            ans += i
        return ans
