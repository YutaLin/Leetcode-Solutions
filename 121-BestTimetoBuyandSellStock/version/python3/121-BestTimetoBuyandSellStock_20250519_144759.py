# Last updated: 5/19/2025, 2:47:59 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[i] > min_price:
                max_profit = max(max_profit, prices[i] - min_price)
            else:
                min_price = prices[i]
        return max_profit
        