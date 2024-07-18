class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        stairs = [i for i in range(n+1)] # [0,1,2,3,5]
        stairs[1] = 1
        stairs[2] = 2

        for i in range(3,n+1):
            stairs[i] = stairs[i-1] + stairs[i-2]
        
        return stairs[n]

        # SC -> O(N)
        # TC -> O(N)
        
        