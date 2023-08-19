class Solution:
    def romanToInt(self, s: str) -> int:
        # s = "MCMXCIV"
        # 0 + 1000 = 1000
        # 1000 - 100 = 900
        # 900 + 1000 = 1900
        # 1900 - 10 = 1890
        # 1890 + 100 = 1990
        # 1990 - 1 = 1989
        # 1989 + 5  = 1994 

        symbol_value =  {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}

        start = 0

        for i in range(len(s) - 1):
            if symbol_value[s[i]] >= symbol_value[s[i+1]]: 
                start += symbol_value[s[i]]
            else:
                start -= symbol_value[s[i]]
        

        return start+symbol_value[s[-1]]

    # SC -> O(1)
    # TC -> O(N)
             


        