class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        def sink(grid,i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return 0

            grid[i][j] = "0"
            # up
            sink(grid,i - 1,j)
            # down
            sink(grid,i + 1,j)
            # left
            sink(grid,i,j - 1)
            #right
            sink(grid,i, j + 1)

            return 1


        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += sink(grid,i,j)

        
        return count


        # SC -> O(N * M)
        # TC -> O(N * M)
        