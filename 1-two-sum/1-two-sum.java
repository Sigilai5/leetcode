class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> element = new HashMap();
        for(int i = 0; i < nums.length;i++){
            int solution = target - nums[i];
            if(element.containsKey(solution)){
                return new int[] {i,element.get(solution)};
            }
            
            element.put(nums[i],i);
            
        }
        
        
        return null;
        
    }
    
    
    
}




