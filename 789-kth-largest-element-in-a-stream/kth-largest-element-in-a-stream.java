class KthLargest {
    private int kLargest;
    private List<Integer> numsList;

    public KthLargest(int k, int[] nums) {
        this.numsList = new ArrayList();
        this.kLargest = k;
        for(int num: nums){
            numsList.add(num);
        }
      
    }
    
    public int add(int val) {
        this.numsList.add(val);
        Collections.sort(this.numsList,Collections.reverseOrder());
        
        return this.numsList.get(this.kLargest-1);
    }
}

// SC -> O(N)
// TC -> O(N Log N)

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */