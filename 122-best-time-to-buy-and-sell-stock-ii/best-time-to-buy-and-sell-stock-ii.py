class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        buy,sell = 0,1

        max_profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit += profit
                buy+=1
            else:
                buy = sell
            
            sell+=1
        
        return max_profit

        # TC -> O(N)
        # SC -> O(1)
        