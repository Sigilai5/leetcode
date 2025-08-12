class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False


        s_list = [0] * 26
        t_list = [0] * 26


        for i in range(len(s)):
            t_list[ord('a') - ord(t[i])] +=1
            s_list[ord('a') - ord(s[i])] +=1
                    
        return s_list == t_list

        # SC -> O(26), O(1)
        # TC -> O(n)



        