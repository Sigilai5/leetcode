class Solution {
    public int climbStairs(int n) {
        if(n <= 3) return n;

        int a = 2;
        int b = 3;

        // 1,2,3,5,8

        for(int i = 0; i < n - 3;i++){
            int temp = a + b;
            
            a = b;
            b = temp;
        }
        
        return b;
    }
}

// SC -> O(1)
// TC -> O(N)