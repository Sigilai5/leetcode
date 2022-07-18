class Solution {
    public int missingNumber(int[] nums) {
        int[] arr_nums = new int[nums.length+1];
        
        
        for(int i = 0; i <= nums.length;i++){
            arr_nums[i] = i;
        }
        
        HashMap<Integer,Integer> numsMap = new HashMap<Integer,Integer>();
        
        for(int num: nums){
            numsMap.put(num,num);
        }
        
        for(int num: arr_nums){
            if(numsMap.containsKey(num) == false){
                return num;
            }
        }
        
        return 0;
        
       
    }
}