class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])



        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != "O":
                return 

            board[row][col] = "B"

            dfs(row,col + 1)
            dfs(row,col - 1)
            dfs(row + 1, col)
            dfs(row - 1, col)


        # Mark all "O" in border

        for row in range(rows):
            if board[row][0] == "O":
                dfs(row,0)
            if board[row][cols - 1] == "O":
                dfs(row,cols - 1)
        
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0,col)
            if board[rows - 1][col]:
                dfs(rows - 1,col)
        
        # Replace all "O" that's inside with "X" and mark all "B" in border with "O"

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "B":
                    board[row][col] = "O"


        
        