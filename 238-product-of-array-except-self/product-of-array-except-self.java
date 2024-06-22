class Solution {
    public int[] productExceptSelf(int[] nums) {
        // [1,2,3,4]
        // left = [1,1,2,6]
        // result = [24,12,8,6]

        int[] lNums = new int[nums.length];

        lNums[0] = 1;

        for(int i = 1; i < lNums.length;i++){
            lNums[i] = lNums[i-1] * nums[i-1];
        }

        int rightProd = 1;

        for(int i = lNums.length - 1; i >= 0; i--){
            lNums[i] *= rightProd;
            rightProd *= nums[i];   
        }


        return lNums;        
    }
}

// SC -> O(N)
// TC -> O(N)