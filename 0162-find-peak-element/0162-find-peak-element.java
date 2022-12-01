class Solution {
    public int findPeakElement(int[] nums) {
        if(nums.length == 1) return 0;
        if(nums[0] > nums[1]) return 0;
        if(nums[nums.length - 1] > nums[nums.length - 2]) return nums.length -1;
        
        
        int pointer = 1;
        while(pointer <= nums.length - 2){
            if(nums[pointer] > nums[pointer -1] && nums[pointer] > nums[pointer+1]){
                return pointer;
            }else{
                pointer++;
            }
        }
        
        return -1;
        
    }
}