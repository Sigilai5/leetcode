class Solution {
    public boolean isPowerOfFour(int n) {
        if(n <= 0) return false;
        
        while(n%4 == 0) n = n/4;
        
        return true ? n == 1: false;
        
    }
}