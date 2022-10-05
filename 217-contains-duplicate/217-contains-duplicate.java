class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer,Integer> duplicates = new HashMap();
        for(int i: nums){
            duplicates.put(i,duplicates.getOrDefault(i,0)+1);
        }
        
        for(int i: duplicates.keySet()){
            if(duplicates.get(i) > 1){
                return true;
            }
        }
        
        return false;
    }
}

//Space Complexity -> O(n)
//Time Complexity -> O(n+m)



// class Solution {
//     public boolean containsDuplicate(int[] nums) {
//         HashSet<Integer> uniques = new HashSet();
//         for(int num:nums){
//             if(uniques.contains(num)){
//                 return true;
//             }
            
//             uniques.add(num);
//         }
        
        
//         return false;
        
//     }
// }

//Space Complexity -> O(n)
//Time Complexity -> O(n)