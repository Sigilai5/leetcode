class Solution {
    public int maxProfit(int[] prices) {
        int buy = 0;
        int sell = 1;

        int maxProfit = 0;

        while(sell < prices.length){
            if(prices[sell] > prices[buy]){
                int profit = prices[sell] - prices[buy];
                maxProfit = Math.max(profit,maxProfit);
                sell+=1;
            }else{
                buy=sell;
                sell+=1;
            }
        }

        return maxProfit;
        
    }
}

// TC -> O(N)
// SC -> O(1)