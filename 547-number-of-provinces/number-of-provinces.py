class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: return 0

        # count cities 
        n = len(isConnected)

        # a way of marking visited cities
        visited = [False] * n

        # initialize count
        provinces = 0

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
                else:
                    pass
                
            return 1


        for city in range(n):
            if not visited[city]:
                visited[city] = True
                provinces += dfs(city)

        return provinces
        
        # SC -> O(M * N)
        # TC -> O(M * N)
        