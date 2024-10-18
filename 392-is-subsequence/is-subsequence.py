class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True

        subCount = 0

        for i in range(len(t)):
            if s[subCount] == t[i]:
                subCount+=1
            
            if subCount == len(s):
                return True
        

        return False

        # SC -> O(1)
        # TC -> O(N)

        