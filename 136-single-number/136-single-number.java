class Solution {
    public int singleNumber(int[] nums) {
        HashSet<Integer> nums_set = new HashSet();
        int pointer = 0;
        int single_number = 0;
        while(pointer < nums.length){
            if(nums_set.contains(nums[pointer])){
                nums_set.remove(nums[pointer]);
            }else{
                nums_set.add(nums[pointer]);
            }
            
            pointer++;
        }
    
        for(int i : nums_set){
            single_number = i;
            break;
        }
        
        return single_number;
        
    }
}