class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> triplets = new LinkedList<List<Integer>>();
        Arrays.sort(nums);
        
        for(int i = 0; i < nums.length;i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int l = i+1;
            int r = nums.length -1;
            
            while(l < r){
                int threeSum = nums[i] + nums[l] + nums[r];
                if(threeSum > 0){
                    r -= 1;
                }else if(threeSum < 0){
                    l += 1;
                }else{
                    triplets.add(Arrays.asList(nums[i],nums[l],nums[r]));
                    l += 1;
                    while(nums[l] == nums[l-1] && l < r){
                        l += 1;
                    }
                }   
            }
        }
        
    
        return triplets;
        
    }
}