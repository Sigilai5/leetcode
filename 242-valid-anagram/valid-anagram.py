class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sGram = [0] * 26
        tGram = [0] * 26

        for i in range(len(s)):
            sGram[ord(s[i]) - ord('a')]+=1
            tGram[ord(t[i]) - ord('a')]+=1

        
        return sGram == tGram

        # SC -> O(26),O(1)
        # TC -> O(N)
        