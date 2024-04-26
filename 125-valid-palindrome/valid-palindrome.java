class Solution {
    public boolean isPalindrome(String s) {
        String sLower = s.toLowerCase();
        String validS = sLower.replaceAll("\\s+","");
        String result = validS.replaceAll("[^A-Za-z0-9]","");

        int i = 0;
        int j = result.length() - 1;

        while(i < j){
            if(result.charAt(i) == result.charAt(j)){
                i+=1;
                j-=1;
            }else{
                return false;
            }

        }

        return true;
        
    }
}

// SC -> O(N)
// TC -> O(N)