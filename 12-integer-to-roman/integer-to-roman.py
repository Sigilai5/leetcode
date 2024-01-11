class Solution:
    def intToRoman(self, num: int) -> str:
        # num = 1994 -> MXC
        # 994
        # 94
        # 4
        output = ""

        while num != 0:
            if num >= 1000:
                output+="M"
                num = num - 1000
            elif num >= 900:
                output+="CM"
                num = num - 900
            elif num >= 500:
                output+="D"
                num = num - 500
            elif num >= 400:
                output+="CD"
                num = num - 400
            elif num >= 100:
                output+="C"
                num = num - 100
            elif num >= 90:
                output+="XC"
                num = num - 90
            elif num >= 50:
                output+="L"
                num = num - 50
            elif num >= 40:
                output+="XL"
                num = num - 40
            elif num >= 10:
                output+="X"
                num = num - 10
            elif num >= 9:
                output+="IX"
                num = num - 9
            elif num >= 5:
                output+="V"
                num = num - 5
            elif num >= 4:
                output+="IV"
                num = num - 4
            elif num >= 1:
                output+="I"
                num = num - 1
            

        return output



        
        