class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True

        s = s.replace(" ","")
        s = s.lower()

        output = []

        for ch in s:
            if ch.isalnum():
                output.append(ch)

        

        left,right = 0, len(output) - 1

        while left < right:
            if output[left] != output[right]:
                return False
            left+=1
            right-=1

        
        return True

        # SC -> O(N)
        # TC -> O(N*N)        