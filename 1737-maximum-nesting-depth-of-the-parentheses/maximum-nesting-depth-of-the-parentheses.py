class Solution:
    def maxDepth(self, s: str) -> int:
        if s == "" or (len(s) == 1 and (s != '(' or s!= ')')) :
            return 0
        
        
        current_depth = 0
        max_depth = 0

        for char in s:
            if char == '(':
                current_depth+=1
                max_depth = max(max_depth,current_depth)
            elif char == ')':
                current_depth-=1

        return max_depth        