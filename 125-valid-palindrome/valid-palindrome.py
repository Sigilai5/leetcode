class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True

        s = s.replace(" ","")
        s = s.lower()

        output = []

        for ch in s:
            if ch.isalnum():
                output.append(ch)

        
        return output == output[::-1]

        # SC -> O(N)
        # TC -> O(N)
        