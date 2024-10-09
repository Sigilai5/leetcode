class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = s.lower()
        result = []

        for ch in s:
            if ch.isalnum():
                result.append(ch)
        

        return result == result[::-1]
        