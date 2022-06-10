class Solution {
    public int[] twoSum(int[] nums, int target) {
       for(int i = 0; i < nums.length; i++){
           for(int j = i+1; j < nums.length; j++){
           
            int compliment = target - nums[i];
            if(compliment == nums[j]){
                return new int[] {i,j};
            }
       }
       }
        
        return null;
        
    }
    
 
    
}