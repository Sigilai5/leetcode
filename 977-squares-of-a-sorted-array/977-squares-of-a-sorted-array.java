class Solution {
    public int[] sortedSquares(int[] nums) {
        for(int i = 0; i < nums.length;i++){
            nums[i] = nums[i] * nums[i];
        }
        
        for(int i = 0; i < nums.length; i++){
            for(int j = i + 1; j < nums.length; j++){
            if(nums[i] > nums[j]){
                int hold = nums[i];
                nums[i] = nums[j];
                nums[j] = hold;    
            }
        }
        }
        
        
        return nums;
    }
}