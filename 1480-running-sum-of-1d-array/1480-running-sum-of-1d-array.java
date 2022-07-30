class Solution {
    public int[] runningSum(int[] nums) {
       int sum = 0;
       int index = 0;
       
       while(index < nums.length){
           sum = sum + nums[index];
           nums[index] = sum;
           index++;
                      
       }
        
        
        return nums;
    }
}