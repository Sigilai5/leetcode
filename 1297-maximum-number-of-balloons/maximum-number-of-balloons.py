class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_chars = Counter("balloon")
        text_chars = Counter(text)

        lowest = float("inf")

        for l in balloon_chars:
            lowest = min(lowest, text_chars[l] // balloon_chars[l])

        return lowest  

        # SC -> O(N)
        # TC -> O(N)