class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()

        output = []

        for ch in s:
            if ch.isalnum():
                output.append(ch)
        
        l,r = 0,len(output) - 1

        while l < r:
            if output[l] != output[r]:
                return False
            l+=1
            r-=1
        
        return True

        # SC -> O(N)
        # TC -> O(N)
        