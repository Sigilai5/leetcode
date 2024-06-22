class Solution {
    public int[] productExceptSelf(int[] nums) {
        // [1,2,3,4]
        // left = [1,1,2,6]
        // right = [24,12,4,1]
        // result = [24,12,8,6]

        int[] lNums = new int[nums.length];
        int[] rNums = new int[nums.length];

        lNums[0] = 1;

        for(int i = 1; i < lNums.length;i++){
            lNums[i] = lNums[i-1] * nums[i-1];
        }

        rNums[nums.length - 1] = 1;

        for(int i = nums.length - 2; i >= 0;i--){
            rNums[i] = rNums[i+1] * nums[i+1];
        }

        for(int i = 0; i < nums.length;i++){
            nums[i] = lNums[i] * rNums[i];
        }


        return nums;        
    }
}

// SC -> O(N)
// TC -> O(N)