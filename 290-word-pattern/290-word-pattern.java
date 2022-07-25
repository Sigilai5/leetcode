class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] s_arr = s.split(" ");
        HashMap<Character,String> s_map = new HashMap();
        boolean follow = true;
        
        if(s_arr.length != pattern.length()) return false;
            
        for(int i = 0; i < pattern.length(); i++){
            
            char current_char = pattern.charAt(i);
            
            if(s_map.containsKey(current_char)){
                if(!s_map.get(current_char).equals(s_arr[i])){
                    follow = false;
                }
                
            } else {
                if(s_map.containsValue(s_arr[i])){
                    follow = false;
                }
            }
            
            
            s_map.put(current_char,s_arr[i]);
        }
        
    
        
        return follow;
    }
}