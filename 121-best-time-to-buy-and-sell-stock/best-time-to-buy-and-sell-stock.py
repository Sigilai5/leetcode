class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) <= 1:
            return 0
        
        buy,sell = 0, 1

        while sell < len(prices): 
            if prices[sell] < prices[buy]:
                buy = sell
                sell+=1
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit,profit)
                sell+=1

        return max_profit 

        # TC -> O(N)
        # SC -> O(1)
        