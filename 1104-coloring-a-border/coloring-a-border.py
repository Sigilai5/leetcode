class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        visited = set()

        origi = grid[row][col]

        border_cells = []


        def dfs(row,col):
            visited.add((row,col))

            is_border = False

            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            for dr,dc in directions:
                new_r, new_c = row + dr, col + dc

                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                    if grid[new_r][new_c] != origi:
                        is_border = True
                    elif (new_r,new_c) not in visited:
                        dfs(new_r,new_c)
                else:
                    is_border = True

            if is_border:
                border_cells.append((row,col))




        dfs(row,col)

        for r,c in border_cells:
            grid[r][c] = color


        return grid        


        # SC -> O(M * N)
        # TC -> O(M * N)