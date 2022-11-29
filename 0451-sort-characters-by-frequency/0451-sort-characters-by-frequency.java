class Solution {
    public String frequencySort(String s) {
        if(s.length() <= 1) return s;
        
        HashMap<Character,Integer> map = new HashMap();
        
        for(char c: s.toCharArray()){
            map.put(c,map.getOrDefault(c,0)+1);
        } //{t=1,r=1,e=2}
        
        
        
        PriorityQueue<HashMap.Entry<Character,Integer>> pq = new PriorityQueue<>((a,b) -> b.getValue() - a.getValue());
        
        for(HashMap.Entry entry: map.entrySet()){
            pq.add(entry); //[e=2,t=1,r=1]
        }
        
        
        StringBuilder output = new StringBuilder();
        
        while(!pq.isEmpty()){
            HashMap.Entry priority = pq.poll();
            for(int j = 0; j < map.get(priority.getKey()); j++){
                output.append(priority.getKey());
            } 
        }
        
        
        return output.toString();
        
        
    }
}