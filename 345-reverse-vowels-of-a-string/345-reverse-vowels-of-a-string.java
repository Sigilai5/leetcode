import java.util.Arrays; 

class Solution {
    public String reverseVowels(String s) {
        
        int strLength = s.length();
        if(strLength == 1) return s;
        
        HashSet<Character> vowels = new HashSet();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        vowels.add('A');
        vowels.add('E');
        vowels.add('I');
        vowels.add('O');
        vowels.add('U');
        
        int l_pointer = 0;
        int r_pointer = strLength - 1;
        
        char[] sArray = s.toCharArray();
        
        while(l_pointer < r_pointer){
            while(l_pointer < r_pointer && vowels.contains(sArray[l_pointer]) != true){
                l_pointer++;
            }
            
            while(l_pointer < r_pointer && vowels.contains(sArray[r_pointer]) != true){
                r_pointer--;
            }
            
            char hold = sArray[l_pointer];
            sArray[l_pointer] = sArray[r_pointer];
            sArray[r_pointer] = hold;
            
            l_pointer++;
            r_pointer--;
        }
        
        
        String final_string = new String(sArray);
        
        return final_string;
        
    }
}