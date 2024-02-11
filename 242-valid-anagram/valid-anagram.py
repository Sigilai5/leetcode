class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_result = [0] * 26
        t_result = [0] * 26

        for i in range(len(s)):
            s_result[ord('a') - ord(s[i])]+=1
            t_result[ord('a') - ord(t[i])]+=1

        return s_result == t_result
        
        # TC -> O(N)
        # SC -> O(N)