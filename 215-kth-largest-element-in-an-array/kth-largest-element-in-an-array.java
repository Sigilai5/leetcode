class Solution {
    public int findKthLargest(int[] nums, int k) {
        Queue<Integer> queue = new PriorityQueue<>((a,b) -> b - a);

        for(int num : nums){
            queue.add(num);
        }
        

        for(int i = 0; i < k -1;i++){
            queue.poll();
        }

        return queue.poll();
        
    }
}

// SC -> O(N)
// TC -> O(N Log K)