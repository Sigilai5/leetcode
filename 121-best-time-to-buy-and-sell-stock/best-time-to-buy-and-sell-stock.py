class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy,sell = 0,1

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                maxProfit = max(maxProfit,prices[sell]-prices[buy])
            else:
                buy = sell
            sell+=1


        return maxProfit 
        # SC -> O(1)
        # TC -> O(n) 