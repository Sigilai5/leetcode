class Solution:
    def removeStars(self, s: str) -> str:
        stack = [s[0]]
        
        for i in range(1,len(s)):
            if s[i] == "*":
                if len(stack) > 0:
                    stack.pop(-1)
            else:
                stack.append(s[i])

        return "".join(stack)


    # SC -> O(N)
    # TC -> O(N)
         