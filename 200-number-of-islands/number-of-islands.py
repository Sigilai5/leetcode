class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # handle the edges cases 
        
        number_of_island = 0
        ROWS, COLS = len(grid), len(grid[0])
                
        #exploration - recursive dfs
        def explore(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != "1":
                return 
            #mark 
            grid[row][col] = "0"
            
            offset = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for nei_offset in offset:
                explore(row +  nei_offset[0], col + nei_offset[1]) 
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] is "1":
                    explore(r, c)
                    number_of_island += 1

        
        return number_of_island
        



