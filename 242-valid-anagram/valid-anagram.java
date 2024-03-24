class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        int[] s_store = new int[26];
        int[] t_store = new int[26];


        for(int i = 0; i < s.length();i++){
            s_store[s.charAt(i) - 'a']++;
            t_store[t.charAt(i) - 'a']++;
        }

        return Arrays.equals(s_store,t_store);           

        
    }
}

// SC -> O(26)
// TC -> O(N)