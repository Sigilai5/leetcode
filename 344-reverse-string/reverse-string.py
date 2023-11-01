class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) <= 1: return s

        l,r = 0, len(s) -1

        while l < r:
            hold = s[l]
            s[l] = s[r]
            s[r] = hold
            l+=1
            r-=1

        return s

        # SC -> O(1)
        # TC -> O(N)

        