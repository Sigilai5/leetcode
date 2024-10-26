class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in ['(','[','{']:
                stack.append(ch)
            elif stack and ch == ')' and stack[-1] == '(':
                stack.pop(-1)
            elif stack and ch == '}' and stack[-1] == '{':
                stack.pop(-1)
            elif stack and ch == ']' and stack[-1] == '[':
                stack.pop(-1)
            else:
                return False   
        
        if len(stack) == 0: return True

        return False

        #  SC -> O(N)
        #  TC -> O(N) 