class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_output =[char for char in s.lower().replace(" ","") if char.isalnum()]

        return s_output == s_output[::-1]
        
        # SC -> O(N)
        # TC -> O(N)