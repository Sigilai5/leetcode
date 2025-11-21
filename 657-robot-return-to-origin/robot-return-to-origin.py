class Solution:
    def judgeCircle(self, moves: str) -> bool:
        rows, cols = 0, 0


        for move in moves:
            if move == 'U':
                rows -= 1
            elif move == 'D':
                rows += 1
            elif move == 'L':
                cols -= 1
            elif move == 'R':
                cols +=1
        

        if rows == 0 and cols == 0: return True


        return False
        

        # SC -> O(1)
        # TC -> O(N)