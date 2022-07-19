class Solution {
    public int maxProfit(int[] prices) {
    
    if(prices.length == 1) return 0;
        
    int left_p = 0;
    int right_p = 1;
    int max_profit = 0;
    
    while(right_p < prices.length){
        if(prices[left_p] > prices[right_p]){
            left_p = right_p;
            right_p+=1;
        }else{
            int total = prices[right_p] - prices[left_p];
            max_profit = Math.max(max_profit,total);
            right_p+=1;
        }
        
       
    }
        
        return max_profit;
}
}



