# 762. Prime Number of Set Bits in Binary Representation https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# Runtime: 151 ms
# Memory Usage: 16.08 MB
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # 10^6 -> 20 bit binary
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19]
        count = 0
        for i in range(left, right+1):
            if bin(i).count("1") in prime_list: count+=1
        return count
