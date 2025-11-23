class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows = len(grid)
              

        def dfs(grid,r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == 0:
                return 1

            if grid[r][c] == 2:
                return 0 

            grid[r][c] = 2

            perimeter = 0
            perimeter += dfs(grid,r - 1,c)
            perimeter += dfs(grid,r + 1,c) 
            perimeter += dfs(grid,r,c - 1)
            perimeter += dfs(grid,r ,c + 1)

            return perimeter


            # SC -> O(R * C)
            # TC -> O(R * C)





        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return dfs(grid,r,c)

        
        return 0
        