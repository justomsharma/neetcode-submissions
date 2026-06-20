class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    sell_profit = max(sell_profit, profit)
        
        return sell_profit
        