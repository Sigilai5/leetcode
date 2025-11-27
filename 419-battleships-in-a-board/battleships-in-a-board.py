class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board: return 0

        ships = 0

        def sink(board,i,j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] == ".":
                return 0

            
            board[i][j] = "."
            # up
            sink(board,i - 1, j)
            # down
            sink(board, i + 1, j)
            # left
            sink(board, i, j - 1)
            # right
            sink(board, i, j + 1)

            return 1



        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    ships += sink(board,i,j)

        
        return ships
        