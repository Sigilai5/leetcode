class Solution {
    public int missingNumber(int[] nums) {
          if(nums.length < 1) return -1;
          if(nums.length == 1 && nums[0] == 0) return 1;  
          if(nums.length == 1 && nums[0] == 1) return 0;  
                 
        
          HashSet<Integer> missing = new HashSet();
        
          for(int i = 1; i <= nums.length; i++){   
              missing.add(i);                         // [1,2,3]
          }  
        
          for(int i: nums){                             //[3,0,1]
              if(missing.contains(i)){
                  missing.remove(i);                     //[2]
              }
          } 
        
        
          if(missing.isEmpty()) return 0;  
           
          return missing.stream().findFirst().get();
        
        
        
        
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