class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_output =[char for char in s.lower().replace(" ","") if char.isalnum()]

        i,j = 0, len(s_output) - 1

        while i < j:
            if s_output[i] == s_output[j]:
                i+=1
                j-=1
            else:
                return False
        

        return True
        

        # SC -> O(N)
        # TC -> O(N)