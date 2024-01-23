class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) == 1: return s

        output = []

        for char in s:
            if char != "*":
                output.append(char) # [l,e,e,t]
            else:
                output.pop(-1)

        
        return "".join(output)

        # SC -> O(N)
        # TC -> O(N)

        