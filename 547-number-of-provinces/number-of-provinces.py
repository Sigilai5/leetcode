class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: return 0

        provinces = 0

        n = len(isConnected)

        visited = [False] * n

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True

                    dfs(neighbor)
                    


        for city in range(n):
            if not visited[city]:
                visited[city] = True

                provinces += 1

                dfs(city)
        

        return provinces
        

        # SC -> O(N)
        # TC -> O(N * N)