# 5. Longest Palindromic Substring https://leetcode.com/problems/longest-palindromic-substring/
# Runtime: 84 ms
# Memory Usage: 16.40 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        transform = '#'.join('^{}$'.format(s))
        p = [0 for i in transform]
        c = 0
        r = 0
        max = 0
        center = 0

        for i in range(1, len(transform)-1):
            p[i] = (r>i) and (min(r-i, p[2*c-i]))
            while transform[i+1+p[i]] == transform[i-1-p[i]]:
                p[i] += 1
            
            if i+p[i] > r:
                c,r = i, i+p[i]
                if p[i]>max:
                    max = p[i]
                    center = i
        
        print(max, center)
        return s[(center-max)//2:(center+max)//2]