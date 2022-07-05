class Solution {
    public int maxProfit(int[] prices) {
      int left = 0;
      int right = 1;
      int maxProfit = 0;
      while(right < prices.length){
          if(prices[right] > prices[left]){
              int profitMade = prices[right] - prices[left];
              maxProfit = Math.max(maxProfit,profitMade);
          }else{
              left = right;
          }
          
          right += 1;
      }
        
        return maxProfit;
        
         
    }
}