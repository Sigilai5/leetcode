class Solution {
    public int searchInsert(int[] nums, int target) {
      int left = 0;  
      int index = 0;  
      while(left < nums.length){
          if(nums[left] == target){
              index = left;
          }
          if(nums[left] < target){
             index = left + 1;
          }
          left++;
      }
        return index;
        
        
    }
}