class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_gram = [0]*26
        t_gram = [0]*26

        for i in range(len(s)):
            s_gram[ord('a') - ord(s[i])]+=1
            t_gram[ord('a') - ord(t[i])]+=1

        
        return s_gram == t_gram

        # SC -> O(26), O(1)
        # TC -> O(N)

        