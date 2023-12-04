class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        max_profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit += profit             
            buy+=1
            sell+=1

        return max_profit


        # SC -> O(1)
        # TC -> O(N)

        