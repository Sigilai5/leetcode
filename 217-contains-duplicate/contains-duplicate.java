class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> unique = new HashSet();

        for(int num:nums){
            if(unique.contains(num)){
                return true;
            }else{
                unique.add(num);
            }
        }

        return false;
        
        
    }
}

// SC -> O(N)
// TC -> O(N)