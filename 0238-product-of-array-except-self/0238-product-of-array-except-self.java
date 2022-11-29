class Solution {
    public int[] productExceptSelf(int[] nums) {
        int numsLen = nums.length;
        
        int[] numsLeft = new int[numsLen];
        int[] numsRight = new int[numsLen];
        
        numsLeft[0] = 1;
        for(int i = 1; i < numsLen; i++){
            numsLeft[i] = nums[i-1] * numsLeft[i-1];   // [1,1,2,6]
        }
        
        numsRight[nums.length -1] = 1;
        for(int i = nums.length - 2; i >= 0; i--){
            numsRight[i] = nums[i+1] * numsRight[i+1];   // [24,12,4,1]
        }
        
      
        for(int i = 0; i < numsLen;i++){
            nums[i] = numsRight[i] * numsLeft[i];
        }
        
        
        return nums;
        
    }
}