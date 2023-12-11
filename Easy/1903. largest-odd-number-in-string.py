# 1903. Largest Odd Number in String https://leetcode.com/problems/largest-odd-number-in-string
# Runtime: 52 ms
# Memory Usage: 18.80 MB
class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[0:i+1]
        return ''
