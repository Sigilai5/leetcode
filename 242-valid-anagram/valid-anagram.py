class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = list(sorted(s))
        t_sorted = list(sorted(t))

        return s_sorted == t_sorted

        # TC O(NLogN)
        # SC -> O(N)
        