class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1}

        if len(s) == 1: return roman_num.get(s)

        output = 0

        for i in range(1,len(s)):
            if roman_num.get(s[i-1]) >= roman_num.get(s[i]):
                output+=roman_num.get(s[i-1])
            else:
                output-=roman_num.get(s[i-1])
        

        return output + roman_num.get(s[-1])    

        # SC -> O(1)
        # TC -> O(N)

        

            
        