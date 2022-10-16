class Solution {
    public int search(int[] nums, int target) {
        int pointer = 0;
        while(pointer < nums.length){
            if(nums[pointer] == target){
                return pointer;
            }
            pointer++;
        }
        
        
        return -1;
        
    }
}