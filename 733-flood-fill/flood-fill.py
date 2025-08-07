class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0] or image[sr][sc] == color: return image

        rows = len(image)
        cols = len(image[0])


        def dfs(row,col,start):
            if (row < 0 or row >= rows or col < 0 or col >= cols or image[row][col] != start):
                return

            image[row][col] = color

            dfs(row + 1,col,start)  
            dfs(row - 1,col,start)

            dfs(row ,col + 1,start)
            dfs(row ,col - 1,start)

        for row in range(rows):
            for col in range(cols):
                if row == sr and col == sc:
                    start = image[row][col]
                    dfs(row, col, start)

        
        return image

        # SC -> O(N), recursion stack
        # TC -> O(R * C)


        