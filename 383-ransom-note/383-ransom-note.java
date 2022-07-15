

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
       // if(ransomNote == magazine) return true;
        
        int[] alphabetArr = new int[26]; //Memory location for all letters in the alphabet
        
        for(char c: magazine.toCharArray()){
            alphabetArr[c - 'a']+=1;                   //By subtracting 'a' we are getting the index of character in the alphabet and increment
        }
        
        for(char c: ransomNote.toCharArray()){
            if(alphabetArr[c - 'a'] == 0){             //Check if character has value in the alphabetArr
                return false;
            }
            
            alphabetArr[c - 'a']-=1;
        }
        
        
        return true;
        
        
    }
}