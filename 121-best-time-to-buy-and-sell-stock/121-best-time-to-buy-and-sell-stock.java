class Solution {
    public int maxProfit(int[] prices) {
      int left= 0, right = 1, maxProfit = 0,profitMade;
      while(right < prices.length){
          if(prices[right] > prices[left]){
              profitMade = prices[right] - prices[left];
              maxProfit = Math.max(maxProfit,profitMade);
          }else{
              left = right;
          }
          
          right += 1;
      }
        
        return maxProfit;
        
         
    }
}