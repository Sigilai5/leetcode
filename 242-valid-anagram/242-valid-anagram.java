class Solution {
    public boolean isAnagram(String s, String t) {        
        HashMap<Character,Integer> sCount = new HashMap();
        HashMap<Character,Integer> tCount = new HashMap();
        
        for(char c: s.toCharArray()){
            sCount.put(c,sCount.getOrDefault(c,0)+1);
        }
        
        
        for(char c: t.toCharArray()){
            tCount.put(c,tCount.getOrDefault(c,0)+1);
        }
        
        
        return sCount.equals(tCount);

    }
}