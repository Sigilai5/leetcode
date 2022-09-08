class Solution {
    public void reverseString(char[] s) {
                
        int l_pointer = 0;
        int r_pointer = s.length - 1;
        
        while(l_pointer < r_pointer){
            char hold = s[l_pointer];
            s[l_pointer] = s[r_pointer];
            s[r_pointer] = hold;
            l_pointer++;
            r_pointer--;
        }
        
    }
}