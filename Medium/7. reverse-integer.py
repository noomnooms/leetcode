# Reverse Integer https://leetcode.com/problems/reverse-integer/
# Runtime: 36 ms
# Memory Usage: 14.2 MB
class Solution:
    def reverse(self, x: int) -> int:
        minn = -2147483648
        maxx = 2147483647

        neg = False
        if x < 0:
            neg = True

        x = str(abs(x))
        x = x[::-1]

        if neg == True:
            if int(x)*-1 < minn:
                return 0
            else:
                return int(x) * -1
        else:
            if int(x) > maxx:
                return 0
            else:
                return int(x)
