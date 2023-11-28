class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return list(sorted(s)) == list(sorted(t)) 

        # TC -> O(NLog(N))
        # SC -> O(N)



        