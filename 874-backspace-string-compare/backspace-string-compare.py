class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for char in s:
            if char != "#":
                s_stack.append(char)
            else:
                if s_stack:
                    s_stack.pop()

        for char in t:
            if char != "#":
                t_stack.append(char)
            else:
                if t_stack:
                    t_stack.pop()


        return s_stack == t_stack

        # SC -> O(N)
        # TC -> O(S + T)        