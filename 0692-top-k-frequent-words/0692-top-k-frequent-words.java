class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        //Better approach
        HashMap<String,Integer> map = new HashMap();
        //["i","love","leetcode","i","love","coding"]
        for(String word: words){
            map.put(word,map.getOrDefault(word,0)+1);
        } 
        //{i=2,love=2,leetcode=1,coding=1}
        
        List<String> output = new ArrayList();
        
        for(String word: map.keySet()){
            output.add(word);
        }
        
       
        Collections.sort(output,(a,b) -> map.get(a).equals(map.get(b)) ? a.compareTo(b) : map.get(b) - map.get(a));
        
        return output.subList(0,k);
        
        
        //Brute Force approach
//         HashMap<String,Integer> map = new HashMap();
//         //["i","love","leetcode","i","love","coding"]
//         for(String word: words){
//             map.put(word,map.getOrDefault(word,0)+1);
//         } 
//         //{i=2,love=2,leetcode=1,coding=1}
        
//         PriorityQueue<HashMap.Entry<String,Integer>> pq = new PriorityQueue<>( (a,b) -> a.getValue().equals(b.getValue()) ? a.getKey().compareTo(b.getKey()) : b.getValue() - a.getValue());
        
        
//         for(HashMap.Entry entry: map.entrySet()){
//             pq.add(entry);
//         }
        
//         List<String> output = new ArrayList();
        
//         for(int i = 0; i < k;i++){
//             output.add(pq.poll().getKey());
//         }
        
        
//         return output;
        
         
        
        
        
    }
}