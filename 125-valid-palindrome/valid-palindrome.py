class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")
        s_arr = []

        for char in s:
            if char.isalnum():
                s_arr.append(char)

        return s_arr == s_arr[::-1]
        