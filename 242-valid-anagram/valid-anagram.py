class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sGram = [0] * 26
        tGram = [0] * 26

        for i in range(len(s)):
            sGram[ord('a') - ord(s[i])]+=1
            tGram[ord('a') - ord(t[i])]+=1
        
        return sGram == tGram


        # SC -> O(26) or O(1)
        # TC -> O(N)
        