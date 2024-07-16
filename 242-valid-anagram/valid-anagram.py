class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_arr = [0] * 26
        t_arr = [0] * 26

        for i in range(len(s)):
            s_arr[ord(s[i]) - ord('a')]+=1

        for i in range(len(t)):
            t_arr[ord(t[i]) - ord('a')]+=1

        
        if s_arr == t_arr: return True

        return False

    # SC -> O(26) -> O(1)
    # TC -> O(N)
        