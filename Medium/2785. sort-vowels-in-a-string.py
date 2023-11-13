# 2785. Sort Vowels in a String https://leetcode.com/problems/sort-vowels-in-a-string/
# Runtime: 225 ms
# Memory Usage: 20.58 MB
class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = []
        for i in s:
            if i in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
                vowels.append(i)

        if len(vowels) > 1:
            vowels.sort()
            v = 0
            for i in (range(len(s))):
                if s[i] in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
                    s[i] = vowels[v]
                    v += 1
        return ''.join(s)
