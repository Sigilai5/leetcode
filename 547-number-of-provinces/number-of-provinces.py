class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected) # 3 cities

        visited = [False] * n # 3 unvisited

        count = 0

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True

                    dfs(neighbor)



        for city in range(n):
            if not visited[city]:
                count += 1
                visited[city] = True

                dfs(city)

        

        return count
        