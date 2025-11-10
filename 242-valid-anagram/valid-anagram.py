class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        countS = [0] * 26

        countT = [0] * 26

        
        for i in range(len(s)):
            countS[ord('a') - ord(s[i])]+=1
            countT[ord('a') - ord(t[i])]+=1             
        
        return countS == countT

        # SC -> O(26) -> O(1)
        # TC -> O(N)