class Solution: 
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,5,3,6,4,0,9]
        if len(prices) < 2: return 0

        buy,sell = 0,1

        max_profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit,profit)
            else:
                buy = sell
            sell += 1

        return max_profit

    # SC -> O(1)
    # TC -> O(N)




