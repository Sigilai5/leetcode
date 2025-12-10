class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows,cols = len(grid), len(grid[0])

        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
                return 0

            grid[row][col] = 0
            area = 1

            area += dfs(row - 1,col)
            area += dfs(row + 1,col)
            area += dfs(row,col - 1)
            area += dfs(row,col + 1)

            return area


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area,dfs(row,col))

        

        return max_area

        # SC -> O(M * N)
        # TC -> O(M * N)
        