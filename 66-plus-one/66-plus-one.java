class Solution {
    public int[] plusOne(int[] digits) {
       for(int i = digits.length - 1; i >= 0; i--){
           if(digits[i] == 9){
               digits[i] = 0;
           }else{
               digits[i] = digits[i] + 1;
               return digits;
           }
           
           
       }
        
       int[] final_digits = new int[digits.length+1];
       final_digits[0] = 1;
        
        return final_digits;
    }
}



