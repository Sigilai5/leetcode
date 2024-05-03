class Solution {
    public int search(int[] nums, int target) {
        int i = 0;
        int j = nums.length - 1;

        while(i <= j){
            int midPoint = (j+i)/2;

            if(nums[midPoint] == target){
                return midPoint;
            }else if(nums[midPoint] < target){
                i+=1;
            }else{
                j-=1;
            }
        }

        return -1;


    }
}

// SC -> O(1)
// TC -> O(Log N)