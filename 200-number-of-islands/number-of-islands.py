class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # initialize count to 0
        count = 0
        # traverse through the rows and columns
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # look for land
                if grid[i][j] == "1":     
                # add 1 to the count
                # sink all land recursively
                    count += self.sink(grid,i,j) 

        return count
    
    def sink(self,grid,i,j):
        if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0"):
            return 0
        
        grid[i][j] = "0" 

        self.sink(grid,i+1,j) # up
        self.sink(grid,i-1,j) # down
        self.sink(grid,i,j+1) # right
        self.sink(grid,i,j-1) # left

        return 1       

        # TC -> O(M * N)
        # SC -> O(M * N)