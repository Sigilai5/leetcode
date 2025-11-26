class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return 0


        def dfs(grid,i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
                return 1

            if grid[i][j] == 2: 
                return 0    

            grid[i][j] = 2
            
            perimeter = 0
            # up
            perimeter += dfs(grid,i - 1,j)
            # down
            perimeter += dfs(grid,i + 1,j)
            # left
            perimeter += dfs(grid,i,j - 1)
            # right
            perimeter += dfs(grid,i,j + 1)

            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return dfs(grid,i,j)

        
        return 0

        # SC -> O(M * N)
        # TC -> O(M * N)
        