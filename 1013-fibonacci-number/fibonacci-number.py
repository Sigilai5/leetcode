class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            last = self.fib(n-1)
            slast = self.fib(n-2)

            return last + slast

            # TC -> O(2N)
            # SC -> O(N)


    # Recursion tree makes this question and any other question related to recursion simpler



        