class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        sArr = s.split()
        return len(sArr[-1])

        # SC -> O(N)
        # TC -> O(N)