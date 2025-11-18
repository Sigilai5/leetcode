class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # initialize count to 0
        count = 0

        def sink(grid,i,j):
                    if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0"):
                        return 0
                    
                    grid[i][j] = "0" 

                    sink(grid,i+1,j) # up
                    sink(grid,i-1,j) # down
                    sink(grid,i,j+1) # right
                    sink(grid,i,j-1) # left

                    return 1   

        # traverse through the rows and columns
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # look for land
                if grid[i][j] == "1":     
                # add 1 to the count
                # sink all land recursively
                    count += sink(grid,i,j)  

        return count
    
            

        # TC -> O(M * N)
        # SC -> O(M * N)