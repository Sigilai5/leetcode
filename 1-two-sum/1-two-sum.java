class Solution {
    public int[] twoSum(int[] nums, int target) {
       
     HashMap<Integer,Integer> numsMap = new HashMap();
     for(int i = 0; i < nums.length; i++){
         int dif = target - nums[i];
         if(numsMap.containsKey(dif)){
             return new int[] {i,numsMap.get(dif)};
         }
         
         numsMap.put(nums[i],i);
     }
        
        
        return null;
        
        
    }
    
   
}





// for(int i = 0; i < nums.length; i++){
//           for(int j = 0; j < nums.length; j++){
//           if(i != j && nums[i] + nums[j] == target){
//               return new int[] {i,j};
//           }
//        }
//        }
        
//         return null;

//Space Complexity => O(1)
//Time Complexity => O(n2)