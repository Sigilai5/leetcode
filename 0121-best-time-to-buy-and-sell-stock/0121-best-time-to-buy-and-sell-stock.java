class Solution {
    public int maxProfit(int[] prices) {
    if(prices.length == 0) return 0;
    
    int maxProfit = 0;
    int left = 0;
    int right = 1;
    while(right < prices.length){
        if(prices[right] > prices[left]){
            int dif = prices[right] - prices[left];
            maxProfit = Math.max(maxProfit,dif);
        }else{
            left = right;
        }
          
        right++;
        
        
    }
         
    if(maxProfit > 0) return maxProfit;
        
    return 0;    
  
  }
    
}



