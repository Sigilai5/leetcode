class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()

        result = []

        for ch in s:
            if ch.isalnum():
                result.append(ch)
        
        return result == result[::-1]

    # TC -> O(N)
    # SC -> O(N)

        