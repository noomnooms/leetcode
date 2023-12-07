# 1716. Calculate Money in Leetcode Bank https://leetcode.com/problems/calculate-money-in-leetcode-bank/
# Runtime: 7 ms
# Memory Usage: 13.25 MB
class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(1, n//7+1):
            ans += ((i+6)*(i+7))/2
            if i > 1:
                ans -= ((i-1)*i)/2

        i = n//7+1
        x = n % 7
        return ans + ((i+x-1)*(i+x))/2 - ((i-1)*i)/2
