class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    count += self.sink(grid,r,c)
        
        

        return count

    def sink(self,grid,r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            self.sink(grid,r+1,c)
            self.sink(grid,r-1,c)
            self.sink(grid,r,c+1)
            self.sink(grid,r,c-1)

            return 1

    # SC -> O(1)
    # TC -> O(R * C)

        