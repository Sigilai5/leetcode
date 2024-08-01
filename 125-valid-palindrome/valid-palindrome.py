class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")
        s_arr = []

        for char in s:
            if char.isalnum():
                s_arr.append(char)

        left = 0
        right = len(s_arr) - 1

        while left < right:
            if s_arr[left] != s_arr[right]:
                return False
            
            left+=1
            right-=1

        return True

        # SC -> O(N)
        # TC -> O(N)
        