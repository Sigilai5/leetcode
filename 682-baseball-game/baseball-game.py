class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
      
        for char in operations:
            if char == '+':
                result.append(result[-1] + result[-2])
            elif char == 'D':
                result.append(result[-1]*2)
            elif char == 'C':
                result.pop(-1)
            else:
                result.append(int(char))
        
        
        return sum(result)
        # SC -> O(N)
        # TC -> O(N)