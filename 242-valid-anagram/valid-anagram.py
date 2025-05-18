class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_arr = [0] * 26
        t_arr = [0] * 26

        for i in range(len(s)):
            s_arr[ord('a') - ord(s[i])]+=1
            t_arr[ord('a') - ord(t[i])]+=1
        
        return s_arr == t_arr

        # SC -> O(26) -> O(1)
        # TC -> O(N)


        