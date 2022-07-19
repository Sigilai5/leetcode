class Solution {
    public int maximumDifference(int[] nums) {
        int left_p = 0;
        int right_p = 1;
        int max_dif = 0;
        
        while(right_p < nums.length){
            if(nums[left_p] > nums[right_p]){
                left_p = right_p;
                right_p++;
            }else{
                int dif = nums[right_p] - nums[left_p];
                max_dif = Math.max(max_dif,dif);
                right_p++;
            }
            
        }
        
        if(max_dif > 0) return max_dif;
        
        return -1;
        
    }
}