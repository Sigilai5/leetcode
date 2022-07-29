class Solution {
    public void moveZeroes(int[] nums){ 
        int counter = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] != 0){
                nums[counter] = nums[i];
                counter++;
            }
        }
        
        for(int i = counter; i < nums.length;i++){
            nums[i] = 0;
        }
        
    }
} 