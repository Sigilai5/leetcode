class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1: return True
        s = s.replace(" ","").lower()

        output = []

        for ch in s:
            if ch.isalnum():
                output.append(ch)

        
        i,j = 0, len(output) - 1

        while i <= j:
            if output[i] != output[j]:
                return False
            
            i+=1
            j-=1
        

        return True

        

        