class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0

        count = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()


        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != "1" or (row,col) in visited:
                return 
            
            grid[row][col] = 0

            visited.add((row,col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            return 1


        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    count += dfs(row,col)


        return count

        # SC -> O(1)
        # TC -> O(R * C)


        