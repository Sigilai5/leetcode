class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 0) return prices[0];

        int maxProfit = 0;
        int buy = 0;
        int sell = 1;

        while(sell < prices.length){
            if(prices[sell] <= prices[buy]){
                buy = sell;
            } else{
                int profit = prices[sell] - prices[buy];
                maxProfit = Math.max(maxProfit,profit);
            }
            sell+=1;
        }

        return maxProfit;
        
    }
}