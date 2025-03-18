class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sCount = [0] * 26
        tCount = [0] * 26

        for i in range(len(s)):
            sCount[ord(s[i]) - ord('a')]+=1
            tCount[ord(t[i]) - ord('a')]+=1 


        return sCount == tCount


        # SC -> O(26) -> O(1)
        # TC -> O(N)
        