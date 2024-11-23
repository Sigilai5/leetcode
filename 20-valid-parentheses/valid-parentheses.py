class Solution:
    def isValid(self, s: str) -> bool:
        output = []

        for ch in s: # s = "([])"
            if ch == "(" or ch == "[" or ch == "{":
                output.append(ch) # ["(","["]
            elif output and output[-1] == "(" and ch == ")":
                output.pop(-1)
            elif output and output[-1] == "[" and ch == "]":
                output.pop(-1)
            elif output and output[-1] == "{" and ch == "}":
                output.pop(-1)
            else:
                return False
        

        if len(output) == 0: return True

        return False

        # SC -> O(N)
        # TC -> O(N)