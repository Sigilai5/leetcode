class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        count = 0

        rows = len(grid)
        cols = len(grid[0])


        def sink(grid,r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return 0

            grid[r][c] = "0"

            queue = deque()
            queue.append((r,c))

            while queue:
                i,j = queue.popleft()

                directions = [[-1,0],[1,0],[0,-1],[0,1]]
        
                for dr, dc in directions:

                    new_r = i + dr
                    new_c = j + dc

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1":
                        grid[new_r][new_c] = "0"
                        queue.append((new_r,new_c))
            
            return 1



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += sink(grid,r,c)

        
        return count

        # SC -> O(M * N)
        # TC -> O(M * N)

        