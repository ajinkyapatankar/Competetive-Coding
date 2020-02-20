class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_price = float("inf")
        min_profit = 0
        for price in prices:
            max_price = min(max_price,price)
            profit = price - max_price
            min_profit = max(profit,min_profit)
        return min_profit