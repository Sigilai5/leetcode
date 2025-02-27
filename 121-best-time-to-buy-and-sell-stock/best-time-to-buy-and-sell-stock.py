class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        max_profit = 0
        buy,sell = 0,1

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit,profit)
                sell+=1
            else:
                buy = sell
                sell+=1
            
        return max_profit

        # SC -> O(1)
        # TC -> O(N)

        