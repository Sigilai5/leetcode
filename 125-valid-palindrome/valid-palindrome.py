class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()

        result = []

        for word in s:
            if word.isalnum():
                result.append(word)

        return result == result[::-1]

        # SC -> O(N)
        # TC -> O(N)
        