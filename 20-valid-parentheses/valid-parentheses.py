class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False

        stack = []

        for par in s:
            if par == "(" or par == "[" or par == "{":
                stack.append(par)
            elif stack and par == ")" and stack[-1] == "(":
                stack.pop(-1)
            elif stack and par == "]" and stack[-1] == "[":
                stack.pop(-1)
            elif stack and par == "}" and stack[-1] == "{":
                stack.pop(-1)
            else:
                return False
        
        if len(stack) == 0: return True

        return False

        # SC -> O(N)
        # TC -> O(N)