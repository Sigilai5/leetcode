class Solution {
    public int maxProfit(int[] prices) {
    if(prices.length == 0) return 0;
    
     int maxProfit = 0;
     int buying = 0;
     int selling = 1;
        
      while(selling < prices.length){
          if(prices[selling] > prices[buying]){
              maxProfit = Math.max(maxProfit,prices[selling] - prices[buying]);
              
          }else{
              buying = selling;
          }
          
          selling+=1;
          
      }
        
        
      return maxProfit;
        
        
     //Space Complexity => O(1)
     //Time Complexity => O(N)   
        
  
  }
    
}



