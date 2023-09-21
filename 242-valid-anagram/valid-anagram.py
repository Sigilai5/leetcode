class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_position = [0 for i in range(26)]
        t_position = [0 for i in range(26)]

        for i in range(len(s)):
            s_position[ord('a') - ord(s[i])] +=1
            t_position[ord('a') - ord(t[i])] +=1

        return s_position == t_position


        