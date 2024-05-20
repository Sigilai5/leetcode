class Solution {
    public int climbStairs(int n) {
        if(n <= 3) return n;

        int a = 2;
        int b = 3;

        for(int i = 0; i < n - 3;i++){
            int hold = a + b;
            a = b;
            b = hold;
        }

        return b;
        
    }
}

// SC -> O(1)
// TC -> O(N)