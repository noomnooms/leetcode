# 32. Longest Valid Parentheses https://leetcode.com/problems/longest-valid-parentheses
# Runtime: 19 ms
# Memory Usage: 14.08 MB
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        valid = []
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    if len(valid) > 0 and stack[-1] < valid[-1][0]:
                        valid[-1][0] = stack[-1]
                        valid[-1][1] = i
                    elif len(valid) > 0 and stack[-1] - valid[-1][1] == 1:
                        valid[-1][1] = i
                    else:
                        valid.append([stack[-1], i])

                    stack.pop()

        ans = 0
        if len(valid) > 0:
            valid.sort()
            last = valid[0]
            for i in range(len(valid)):
                if i > 0 and valid[i][0]-last[1] == 1:
                    last[1] = valid[i][1]
                elif valid[i][0] > last[1]+1:
                    last = valid[i]
                ans = max(ans, last[1]-last[0]+1)

        return ans
