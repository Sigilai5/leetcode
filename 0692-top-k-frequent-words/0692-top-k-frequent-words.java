class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String,Integer> map = new HashMap();
        
        //["i","love","leetcode","i","love","coding"]
        for(String c: words){
            map.put(c,map.getOrDefault(c,0)+1);
        }
        //{i=2,love=2,leetcode=1,coding=1}
        
        
        PriorityQueue<HashMap.Entry<String,Integer>> pq = new PriorityQueue<>((a,b) -> a.getValue().equals(b.getValue()) ? a.getKey().compareTo(b.getKey()) : b.getValue() - a.getValue()); //FIFO
        
        
        for(HashMap.Entry entry: map.entrySet()){
            pq.add(entry);
        }
        
        //[i=2,love=2,leetcode=1,coding=1]
        
        List<String> output = new ArrayList();
        
        for(int i = 0; i < k; i++){
            output.add(pq.poll().getKey());
        }
        
        //["i","love"]
  
        
        return output;
        
        
        
    }
}