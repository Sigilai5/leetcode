class Solution {
    public int searchInsert(int[] nums, int target) {
      int left = 0; 
      int right = 0;  
      int counter = 0;  
      int nums_length = nums.length - 1;
      while(left <= nums_length){
          
          if(nums[left] == target){
              counter = left;
           
          }
          
          if(nums[left] < target){
             counter = left + 1;
  
          }
          
          
          
          left++;
      }
        
               
        
        
        
        return counter;
        
        
    }
}