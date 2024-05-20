class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)-> b - a); 

        for(int stone: stones) pq.add(stone);
        while(pq.size() > 1) pq.add(pq.poll() - pq.poll());

        return pq.poll();
        
    }
}