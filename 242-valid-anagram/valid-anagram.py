class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sGrams = [0] * 26
        tGrams = [0] * 26


        for i in range(len(s)):
            sGrams[ord('a') - ord(s[i])]+=1
            tGrams[ord('a') - ord(t[i])]+=1
        

        return sGrams == tGrams

    # SC -> O(26)
    # TC -> O(N)
        