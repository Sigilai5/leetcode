class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]",""); //remove all non-alphanumeric characters.
        s = s.toLowerCase();
        // s = s.replaceAll("\\s","");  //Remove whitespaces
        char sArr[] = s.toCharArray();
        char rArr[] = new char[sArr.length];
        int pointer = 0;
        for(int i = sArr.length - 1; i >= 0;i--){
            rArr[pointer] = sArr[i];
            pointer++;
        }
        
        boolean isPalindrome = Arrays.equals(sArr,rArr);
        return isPalindrome;
        
        //Space Complexity -> O(m+n)
        //Time Complexity -> O(n)
        
        /*Method 2*/
//         if(s == "") return true;
       
//        String newString = s.toLowerCase();
//        String removedAlpha = newString.replaceAll("[^A-Za-z0-9]","");
       
//        char[] sArray = removedAlpha.toCharArray();
        
//        String finalString = ""; 
        
//        for(int i = sArray.length-1; i>=0; i--){
//            finalString+= sArray[i];
//        } 
        
        
//         return finalString.equals(removedAlpha);
        
        //Space Complexity -> O(n)
        //Time Complexity -> O(n)
        
    }
}