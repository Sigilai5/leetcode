class Solution(object):
    def isPalindrome(self, x):
        y = list(str(x))
        pal_array = []
        for i in y:
            pal_array.append(i)
        if pal_array == pal_array[::-1]:
            return True
            
        