class Solution {
    public int[] topKFrequent(int[] nums, int k) {
    //1.Get element count
    //2.Append to priority queue based on value;
    //3.Get k top elements in the priority queue
        
    HashMap<Integer,Integer> map = new HashMap<>();
        
    for(int i: nums){
        map.put(i,map.getOrDefault(i,0)+1);
    }    
        
    PriorityQueue<HashMap.Entry<Integer,Integer>> pq = new PriorityQueue<>((a,b) -> b.getValue() - a.getValue()); //Max Heap
        
    for(HashMap.Entry entry: map.entrySet()){
        pq.add(entry);
    }
        
    int[] output = new int[k];
    for(int i = 0; i < k; i++){
        output[i] = pq.poll().getKey();
    }
        
        
    return output;    
        
        
    //Space Complexity:O(m+n)
    //Time Complexity:O(n)    
        
        
    }
}