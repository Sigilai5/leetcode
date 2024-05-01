class Solution {
    public boolean isPalindrome(String s) {
        String sPace = s.replaceAll("\\s+","");
        String sAlpha = sPace.replaceAll("[^A-Za-z0-9]","");
        String sLower = sAlpha.toLowerCase();

        int i = 0;
        int j = sLower.length() - 1;

        while(i < j){
            if(sLower.charAt(i) != sLower.charAt(j)){
                return false;
            } else{
               i+=1;
               j-=1;
            }
        }

        return true;
        
    }


}

// SC -> O(N)
// TC -> O(N)