class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,0

        max_profit = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit,profit)

            if prices[sell] > prices[buy]:
                sell+=1
            else:
                buy=sell
                sell+=1
        

        return max_profit
    
    # SC -> O(1)
    # TC -> O(N)