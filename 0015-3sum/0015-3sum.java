class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        ArrayList<List<Integer>> result = new ArrayList();
        if(nums == null || nums.length < 3) return result;
        
        Arrays.sort(nums); //Sorting helps in shifting l and r pointers and avoiding duplicates
        
        for(int i = 0; i < nums.length;i++){
            if(i > 0 && nums[i] == nums[i-1]){  
                continue;                      // skip duplicates e.g -3 and -3 in  [-3,-3,0,1,2,2,2]
            }
            
            int first = nums[i];
            int left = i+1;
            int right = nums.length - 1;
            
            while(left < right){
            int threeSum = first + nums[left] + nums[right];
            if(threeSum > 0){
                right--;
            }else if(threeSum < 0){
                left++;
            }else{
                result.add(Arrays.asList(first,nums[left],nums[right]));
                left++;
                while(nums[left] == nums[left-1] && left < right){
                     left++;
                    }
                while(nums[right] == nums[right-1] && left < right){
                     right--;
                    }
                }
            } 
        }
        
        
        return result;
        
        
    }
}

// Time Complexity:O(n^2)
// Space Complexity:O(n)