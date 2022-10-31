class Solution {
    public int missingNumber(int[] nums) {
         if(nums == null) return -1;
        
         HashSet<Integer> unique = new HashSet();
         for(int i: nums){
             unique.add(i);
         } 
        
         for(int i = 0; i<=nums.length;i++){
             if(unique.contains(i) == false){
                 return i;
             }
         }
        
            
        return -1;
        
        
        
        
        
//         int[] arr_nums = new int[nums.length+1];
        
        
//         for(int i = 0; i <= nums.length;i++){
//             arr_nums[i] = i;
//         }
        
//         HashMap<Integer,Integer> numsMap = new HashMap();
        
//         for(int num: nums){
//             numsMap.put(num,num);
//         }
        
//         for(int num: arr_nums){
//             if(!numsMap.containsKey(num)){
//                 return num;
//             }
//         }
        
//         return 0;
        
       
    }
}

//Space Complexity -> O(n+m)
//Time Complexity -> O(n+m+o)