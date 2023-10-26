# 14. Longest Common Prefix https://leetcode.com/problems/longest-common-prefix/
# Runtime: 32 ms
# Memory Usage: 14.4 MB
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)

        prev_common = ''
        for i in range(len(strs[0])):
            common = strs[0][:i+1]
            for j in range(1, len(strs)):
                if strs[j][:i+1] != common:
                    return prev_common
            prev_common = common
        return prev_common
