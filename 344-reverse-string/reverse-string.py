class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) == 1: return s
        left,right = 0, len(s) - 1

        while left < right:
            hold = s[left]
            s[left] = s[right]
            s[right] = hold
            left+=1
            right-=1
        

        return s

        # SC -> O(1)
        # TC -> O(n)



        