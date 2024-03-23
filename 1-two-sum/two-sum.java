class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> result = new HashMap();

        for(int i = 0; i < nums.length;i++){
            int dif = target - nums[i];

            if(result.containsKey(dif)){
                return new int[] {i,result.get(dif)};
            }

            result.put(nums[i],i);

        }

        return new int[] {};
        
    }
}

// SC -> O(1)
// TC -> O(N)