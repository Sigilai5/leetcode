class Solution:
    def fib(self, n: int) -> int:
        # 0,1,1,2,3,5,8,13
        if n == 0: return 0
        elif n == 1: return 1
        else: return self.fib(n-1) + self.fib(n-2)

        # SC -> O(N), recursive stack frames
        # TC -> O(N)
        