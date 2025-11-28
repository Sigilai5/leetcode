class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
   
        def dfs(grid,i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
                return 1

            if grid[i][j] == 2: return 0

            grid[i][j] = 2

            per = 0

            per += dfs(grid,i - 1,j)
            per += dfs(grid,i + 1,j)
            per += dfs(grid,i,j - 1)
            per += dfs(grid,i,j + 1)

            return per

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return dfs(grid,i,j)
        

        return 0

        