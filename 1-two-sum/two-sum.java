class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> lookUp = new HashMap<>();

        for(int i = 0; i < nums.length;i++){
            int compNum = target - nums[i];
            if(lookUp.containsKey(compNum)){
                return new int[] {lookUp.get(compNum),i};
            }

            lookUp.put(nums[i],i); 
        }

        return new int[] {};
        
    }
}

// SC -> O(N)
// TC -> O(N)