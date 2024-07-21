class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        cols = len(grid)
        rows = len(grid[0]) 

        for i in range(cols):
            for j in range(rows):
                if grid[i][j] == '1':
                    count+=self.sink(grid,i,j)


        return count

    def sink(self,grid,i,j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return 0

        grid[i][j] = '0'
        self.sink(grid,i+1,j) 
        self.sink(grid,i-1,j)  
        self.sink(grid,i,j+1) 
        self.sink(grid,i,j-1)

        return 1

    # SC -> O(1)
    # TC -> O(N*M)