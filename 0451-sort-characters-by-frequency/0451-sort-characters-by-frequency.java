class Solution {
    public String frequencySort(String s) {
        if(s.length() == 1) return s;
        
        HashMap<Character,Integer> map = new HashMap();
        
        for(char c: s.toCharArray()){
            map.put(c,map.getOrDefault(c,0)+1);
        }
        
        
        PriorityQueue<HashMap.Entry<Character,Integer>> pq = new PriorityQueue<>((a,b) -> b.getValue() - a.getValue());
        
        for(HashMap.Entry entry: map.entrySet()){
            pq.add(entry);     //{e=2,r=1,t=1}       
        }
        
        
        String output = ""; 
        while(!pq.isEmpty()){ 
            HashMap.Entry c = pq.poll();
            for(int i = 0; i < map.get(c.getKey()); i++){ 
                output+= c.getKey();
            } 
            
        }
         
        
        return output;
        
    }
}