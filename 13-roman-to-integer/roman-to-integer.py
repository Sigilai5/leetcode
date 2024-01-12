class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            "M":1000,
            "CM":900,
            "D":500,
            "CD":400,
            "C":100,
            "XC":90,
            "L":50,
            "XL":40,
            "X":10,
            "IX":9,
            "V":5,
            "IV":4,
            "I":1}

        output = 0

        if len(s) == 1: return roman_num.get(s)

        for i in range(1,len(s)):
            if roman_num.get(s[i-1]) < roman_num.get(s[i]):
                output-=roman_num.get(s[i-1])
            else:
                output+=roman_num.get(s[i-1])


        return output + roman_num.get(s[i])


        # SC -> O(1)

        # TC -> O(N)

            
        