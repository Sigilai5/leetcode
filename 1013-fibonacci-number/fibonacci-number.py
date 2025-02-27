class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            last = self.fib(n-1)
            slast = self.fib(n-2)
            return last + slast

        # SC -> O(N), recursion stack
        # TC -> O(2^N)
        