# 823. Binary Trees With Factors
# Runtime: 2749 ms
# Memory Usage: 16.4 MB
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        log = {i: 1 for i in arr}

        for i in range(1, len(arr)):
            for j in range(0, i):
                if arr[i] % arr[j] == 0 and arr[i]/arr[j] in arr:
                    log[arr[i]] += log[arr[j]]*log[arr[i]/arr[j]]
        return sum(log.values()) % 1000000007
