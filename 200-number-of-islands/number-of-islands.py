class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])

        count = 0

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
                return 0

            grid[i][j] = "0"

            queue = deque()

            queue.append((i,j))

            while queue:
                r,c = queue.popleft()

                directions = [[-1,0],[1,0],[0,-1],[0,1]]


                for dr,dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1":
                        grid[new_r][new_c] = "0"
                        queue.append((new_r,new_c))
            
            return 1


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += dfs(i,j)
        

        return count

        # SC -> O(M * N)
        # TC -> O(M * N)
        