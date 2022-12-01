class Solution {
    public int findPeakElement(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> b - a);
        
        for(int num:nums){
            pq.add(num);
        }
        
        int max = pq.poll();
        
        int pointer = 0;
        
        while(pointer < nums.length){
            if(nums[pointer] == max){
                return pointer;
            }
            pointer++;
        }
        
        
        return -1;
        
    }
}