import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        char sArr[] = s.toCharArray();        
        char tArr[] = t.toCharArray();
        
        Arrays.sort(sArr);
        Arrays.sort(tArr);
        
        
        
        boolean compareArr = Arrays.equals(sArr,tArr);
        return compareArr;
        
       

    }
}