class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        col = len(grid)
        rows = len(grid[0])

        for i in range(col):
            for j in range(rows):
                if grid[i][j] == '1':
                    count+=self.sink(i,j,grid)
        
        return count
        

        
    def sink(self, i,j,grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) >= 0 or grid[i][j] == '0':   
            return 0
     
        grid[i][j] = '0'
        self.sink(i+1,j,grid)
        self.sink(i-1,j,grid)
        self.sink(i,j+1,grid)
        self.sink(i,j-1,grid)
        return 1


    # SC -> O(1)
    # TC -> O(N*M)