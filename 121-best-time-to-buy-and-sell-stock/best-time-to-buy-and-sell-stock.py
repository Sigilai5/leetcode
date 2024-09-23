class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        buy,sell = 0,1

        max_profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
                sell+=1
            else:
                buy = sell
                sell+=1
        

        return max_profit

        