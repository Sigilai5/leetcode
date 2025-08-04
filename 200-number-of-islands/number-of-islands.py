class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows = len(grid)
       
        visited = set()

        count = 0

        def sink(row,col):
            if (row < 0 or row >= rows or col < 0  or col >= len(grid[row]) or grid[row][col] == "0" or (row,col) in visited):
                return
            
            visited.add((row,col))

            sink(row-1,col) 
            sink(row+1,col) 
            sink(row,col+1)
            sink(row,col-1)

            return 1

            
        

        for row in range(rows):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and (row,col) not in visited:
                   count +=  sink(row,col)
                    
                    
        

        return count


    # SC -> O(N)
    # TC -> O(R * C)
        