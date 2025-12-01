class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])

        ships = 0

        def sink(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != "X":
                return 0 

            board[row][col] = "."

            sink(row - 1,col)
            sink(row + 1,col)
            sink(row,col - 1)
            sink(row,col + 1)

            return 1

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "X":
                    ships += sink(row,col)


        return ships

        # SC -> O(M * N)
        # TC -> O(M * N)

        