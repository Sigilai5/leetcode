class Solution {
    public int singleNumber(int[] nums) {
        if(nums.length == 1) return nums[0];
        
        HashSet<Integer> unique_set = new HashSet();
        
        for(int i : nums){
            if(unique_set.contains(i)){
                unique_set.remove(i);
            }else{
                unique_set.add(i);
            }
            
            
        }
        
        
        return unique_set.stream().findFirst().get();
        
    }
}