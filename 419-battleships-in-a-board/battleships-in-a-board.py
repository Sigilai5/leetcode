class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows,cols = len(board), len(board[0])

        count = 0

        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != "X":
                return 0

            board[row][col] = "."

            queue = deque()
            queue.append((row,col))

            while queue:
                r,c = queue.popleft()

                directions = [[-1,0],[1,0],[0,-1],[0,1]]

                for dr,dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] == "X":
                        board[new_r][new_c] = "."
                        queue.append((new_r,new_c))

            
            return 1



        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "X":
                    count += dfs(row,col)
        

        return count

        # SC -> O(M * N)
        # TC -> O(M * N)
        