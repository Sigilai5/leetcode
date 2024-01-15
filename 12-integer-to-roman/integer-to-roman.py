class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbol = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",
                     40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}

        output = ""
        
        for value, symbol in value_symbol.items():
            while num >= value:
                output+=symbol
                num = num - value
        

        return output



        # SC -> O(1)
        # TC -> O(N)

        