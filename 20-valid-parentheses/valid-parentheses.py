class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif stack and char == ')' and stack[-1] == '(':
                stack.pop(-1)
            elif stack and char == '}' and stack[-1] == '{':
                stack.pop(-1)
            elif stack and char == ']' and stack[-1] == '[':
                stack.pop(-1)
            else:
                return False   
        

        if stack: return False

        return True

        # TC -> O(N)
        # SC -> O(N)