class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> dset = new HashSet<Integer>();
        for(final int num: nums){
            dset.add(num);
        }
        
        if(dset.size() == nums.length) return false;
        
        return true;
        
    }
}