class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;
           

        int[] store = new int[26];


        for(int i = 0; i < s.length();i++){
            store[s.charAt(i) - 'a']++;
            store[t.charAt(i) - 'a']--;
        }

        int[] compare = new int[26];

        return Arrays.equals(store,compare);           

        
    }
}

// SC -> O(26)
// TC -> O(N)