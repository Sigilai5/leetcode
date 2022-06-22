class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> dset = new HashSet<Integer>();
        for(final int num: nums){
            if(dset.contains(num)){
                return true;
            }
            
            dset.add(num);
        }
        
        return false;
        
    }
}