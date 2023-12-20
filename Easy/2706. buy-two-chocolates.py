# 2706. Buy Two Chocolates https://leetcode.com/problems/buy-two-chocolates/
# Runtime: 72 ms
# Memory Usage: 16.20 MB
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        return money if prices[0]+prices[1] > money else money-prices[0]-prices[1]
