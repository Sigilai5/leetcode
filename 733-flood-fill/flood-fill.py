from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0] or image[sr][sc] == color:
            return image

        def dfs(image, i, j, start):
            if (i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or 
                image[i][j] != start):
                return

            image[i][j] = color
            # up
            dfs(image, i - 1, j, start)
            # down
            dfs(image, i + 1, j, start)
            # left
            dfs(image, i, j - 1, start)
            # right
            dfs(image, i, j + 1, start)

        for i in range(len(image)):
            for j in range(len(image[i])):
                if i == sr and j == sc:  # Fixed: j == sc
                    start = image[i][j]
                    dfs(image, i, j, start)
                    return image

        return image