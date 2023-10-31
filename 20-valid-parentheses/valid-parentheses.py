class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif stack and stack[-1] == '(' and char == ')':
                stack.pop(-1)
            elif stack and stack[-1] == '[' and char == ']':
                stack.pop(-1)
            elif stack and stack[-1] == '{' and char  == '}':
                stack.pop(-1)
            else:
                return False
        
        if len(stack) == 0: return True

        return False
        