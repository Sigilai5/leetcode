class Solution {
    public boolean isPowerOfThree(int n) {
        if(n == 0 || n < 0) return false;
        
        while(n%3 == 0) n = n/3;
        
        return true ? n == 1: false;
    }
}