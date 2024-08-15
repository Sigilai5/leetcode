class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += self.sink(grid,i,j)
        
        return count
    
    def sink(self,grid,i,j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != "1":
            return 0
        
        grid[i][j] = "0"
        self.sink(grid,i+1,j)
        self.sink(grid,i-1,j)
        self.sink(grid,i,j+1)
        self.sink(grid,i,j-1)
        return 1
    
    # SC -> O(1)
    # TC -> O(N*M)
        