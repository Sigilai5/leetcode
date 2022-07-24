class Solution {
    public boolean isSubsequence(String s, String t) {
    
        if(s.isEmpty()) return true;
        
        int is_subcount = 0;
        for(int i = 0; i < t.length();i++){
            if(s.charAt(is_subcount) == t.charAt(i)){
                is_subcount++;
             if(is_subcount == s.length()) return true;
            }
        }
        
        return false;
        
    }
}