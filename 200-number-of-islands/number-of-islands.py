class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        count = 0

        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != "1":
                return 0

            grid[row][col] = "0"
            queue = deque()
            queue.append((row,col))

            while queue:
                r,c = queue.popleft()

                directions = [[-1,0],[1,0],[0,-1],[0,1]]

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1":
                        grid[new_r][new_c] = "0"
                        queue.append((new_r,new_c))
            

            return 1


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += dfs(row,col)

        
        return count

        # TC -> O(M * N)
        # SC -> O(M * N)




        