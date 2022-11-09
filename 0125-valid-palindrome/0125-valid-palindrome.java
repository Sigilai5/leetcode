class Solution {
    public boolean isPalindrome(String s) {
       if(s == "") return true;
       
       String newString = s.toLowerCase();
       String removedAlpha = newString.replaceAll("[^A-Za-z0-9]","");
       
       char[] sArray = removedAlpha.toCharArray();
        
       String finalString = ""; 
        
       for(int i = sArray.length-1; i>=0; i--){
           finalString+= sArray[i];
       } 
        
        
      
        
        return finalString.equals(removedAlpha);
        
    }
}