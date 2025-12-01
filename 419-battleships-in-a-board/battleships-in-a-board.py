class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])

        ships = 0

        def sink(row,col):
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != "X":
                return 0

            board[row][col] = "."

            queue = deque()
            queue.append((row,col))

            while queue:
                r,c = queue.popleft()

                directions = [[0,-1],[-1,0],[1,0],[0,1]]

                for dr,dc in directions:
                    nr,nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "X":
                        board[nr][nc] = "."
                        queue.append((nr,nc))
            
            return 1



        for row in range(rows):
            for col in range(cols):
                ships+=sink(row,col)

        
        return ships

        # SC -> O(M * N)
        # TC -> O(M * N)
        