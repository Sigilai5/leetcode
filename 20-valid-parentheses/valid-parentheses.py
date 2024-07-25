class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            elif stack and ch == '}' and stack[-1] == '{':
                stack.pop()
            elif stack and ch == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and ch == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False

        if len(stack) != 0: return False
        
        return True

        # SC -> O(N)
        # TC -> O(N)
        