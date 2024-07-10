class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) == 1): return 0

        buy = 0
        sell = 1

        maxProfit = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit,profit)

            if prices[buy] > prices[sell]:
                buy = sell

            sell+=1

        return maxProfit 
             
        ## SC -> O(1)
        ## TC -> O(N)
        