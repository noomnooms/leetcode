# 20. Valid Parentheses https://leetcode.com/problems/valid-parentheses/
# Runtime: 11 ms
# Memory Usage: 13.4 MB
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = ''
        for i in s:
            if i in '([{':
                queue += i
            elif len(queue)==0: return False
            
            if i in ')':
                if queue[-1] != '(': return False
                queue = queue[:-1]
            if i in ']':
                if queue[-1] != '[': return False
                queue = queue[:-1]
            if i in '}':
                if queue[-1] != '{': return False
                queue = queue[:-1]
                
        if len(queue)>0: return False
        return True
