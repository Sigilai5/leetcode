class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        total = []
        buy,sell = 0,1

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                total.append(profit)
                buy+=1
                sell+=1
            else:
                buy = sell
                sell+=1
        

        sum_total = sum(total)
        return sum_total\

        # TC -> O(N)
        # SC -> O(N)
        