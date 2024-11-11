class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = list(sorted(s))
        tArr = list(sorted(t))

        return sArr == tArr


        # SC -> O(N)
        # TC -> O(N)
        