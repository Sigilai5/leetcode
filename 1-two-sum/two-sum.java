class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer>  check = new HashMap();

        for(int i = 0; i < nums.length;i++){
            int dif = target - nums[i];

            if(check.containsKey(dif)){
                return new int[] {i,check.get(dif)};
            }

            check.put(nums[i],i);
        }


        return new int[] {};
        
    }
}

// SC -> O(N)
// TC -> O(N)

