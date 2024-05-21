class KthLargest {
    int k;
    PriorityQueue<Integer> pq;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.pq = new PriorityQueue<>((a, b)-> a - b);
        for (int num: nums) this.pq.offer(num);
        System.out.println(this.pq);
    }
    
    public int add(int val) {
        this.pq.offer(val);
        while(this.pq.size() > this.k){
            this.pq.poll();
        }

        return this.pq.peek();
    }
}

// SC -> O(N)
// TC -> O(N)

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */