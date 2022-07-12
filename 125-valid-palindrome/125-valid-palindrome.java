class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]","");
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
        
    }
}