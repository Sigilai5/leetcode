class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # intialize max profit
        max_profit = 0

        buy,sell = 0, 1

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit,profit)
                sell+=1
        
        return max_profit

        # SC -> O(1)
        # TC -> O(N)
                
        

        return max_profit

        