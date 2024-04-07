class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length == 1) return 0;
        int maxProfit = 0;
        int i = 0;
        int j = 1;

        while(j < prices.length){
            int profit = prices[j] - prices[i];
            maxProfit = Math.max(maxProfit,profit);

            if(prices[j] < prices[i]){
                i = j;
            }

            j+=1;

        }

        return maxProfit;
        
    }
}