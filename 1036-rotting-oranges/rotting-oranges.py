class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # check if our grid is empty
        if not grid: return 0
        # step by step initialize our queue to travese through our grid FIFO priority
        queue = deque()
        
        # initialize our fresh count = 0
        fresh_count = 0
        # initalize our min_minute = 0
        min_minute = 0
        # count our fresh oranges
        # queue in our rotten orange position
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i,j,0])
                elif grid[i][j] == 1:
                    fresh_count+=1
        
        
        if fresh_count == 0: return 0
        # define the directions
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        # maintain if queue is not empty, get current row,col and time
        while queue:
            row,col,time = queue.popleft()
        # compare max time taken
            min_minute = max(min_minute,time)
        # traverse trough the 4 directions 
            for dr,dc in directions:
                r = dr + row
                c = dc + col

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                    #  mark fresh fruit as rotten
                    grid[r][c] = 2
                    # reduce fresh count by 1
                    fresh_count -= 1
                    # add next position in our queue while adding time as 1
                    queue.append([r,c,time+1])
        
        # when queue escapes,check if fresh is zero and return min_minute else return - 1
        return min_minute if fresh_count == 0 else -1



        # SC -> O(M * N)
        # TC -> O(M * N)
        