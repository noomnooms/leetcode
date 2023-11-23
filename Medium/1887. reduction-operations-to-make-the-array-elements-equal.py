# 1887. Reduction Operations to Make the Array Elements Equal https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal
# Runtime: 851 ms
# Memory Usage: 23.52 MB
class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_cnt = {}
        for i in nums:
            try:
                num_cnt[i] += 1
            except:
                num_cnt[i] = 1

        digits = sorted(num_cnt.keys(), reverse=True)
        length = len(digits)-1
        cnt = [num_cnt[digits[i]]*(length-i) for i in range(0, length)]
        return sum(cnt)
