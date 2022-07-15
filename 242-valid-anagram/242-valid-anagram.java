class Solution {
    public boolean isAnagram(String s, String t) {        
        int salphabetArr[] = new int[26];
        int talphabetArr[] = new int[26];
        
        for(char ch: s.toCharArray()){
            salphabetArr[ch - 'a']++;
        } 
        
        for(char ch: t.toCharArray()){
            talphabetArr[ch - 'a']++; 
        }
        
        
        boolean isEqual = Arrays.equals(salphabetArr,talphabetArr);
        
        return isEqual;

    }
}