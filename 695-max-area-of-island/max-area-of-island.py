class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        max_area = 0
        
        def sink(grid,i,j):
            if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0):
                return 0

            grid[i][j] = 0
            area = 1
            # up
            area += sink(grid,i-1,j)
            # down
            area += sink(grid,i+1,j)
            # left
            area += sink(grid,i,j-1)
            # right
            area += sink(grid,i,j+1)

            return area




        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area = max(max_area,sink(grid,i,j))

        
        return  max_area

        # SC -> O(N * M)
        # TC -> O(N * M)
        