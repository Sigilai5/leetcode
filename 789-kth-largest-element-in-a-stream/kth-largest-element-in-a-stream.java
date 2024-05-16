class KthLargest {
    private int kLargest;
    private PriorityQueue<Integer> queue;

    public KthLargest(int k, int[] nums) {
        this.queue = new PriorityQueue();
        this.kLargest = k;
        for(int num: nums){
            this.queue.add(num); 
        }
        
    }
    
    public int add(int val) {
        this.queue.add(val);
        while(!this.queue.isEmpty() && this.queue.size() != this.kLargest){
            this.queue.poll();
        }
        return this.queue.peek();
        
    }
}

// SC -> O(k)
// TC -> O(N Log k)

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */