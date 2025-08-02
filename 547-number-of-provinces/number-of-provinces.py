class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: return 0

        # get cities length
        n = len(isConnected)

        # check if city is visited
        visited = [False] * n

        # count provinces
        count = 0

        def dfs(city):
            for neighbor in range(n): 
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True

                    dfs(neighbor)

        for city in range(n):
            if not visited[city]:
                visited[city] = True

                count +=1

                dfs(city)

        

        return count

        # SC -> O(N) recursion stack plus visited list

        # TC -> O(N*N)

        