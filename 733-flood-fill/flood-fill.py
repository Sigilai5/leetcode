class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        start_color = image[sr][sc]

        visited = set()

        def dfs(row,col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != start_color or (row,col) in visited:
                return

            image[row][col] = color 
            visited.add((row,col))

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)


        for row in range(rows):
            for col in range(cols):
                if (row,col) == (sr,sc) and image[row][col] == start_color and (row,col) not in visited:
                    dfs(row,col)


        return image