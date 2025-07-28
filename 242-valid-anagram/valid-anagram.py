class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return list(sorted(s)) == list(sorted(t))

        # SC -> O(N)
        # TC -> O(N Log N)


        