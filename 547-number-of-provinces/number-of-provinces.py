class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # DEPTH FIRST SEARCH
        if not isConnected: return 0

        # get length of the city
        n = len(isConnected)

        # mark all cities as unvisted
        visited = [False] * n

        # initialize province count
        count = 0

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and visited[neighbor] == False:
                    visited[neighbor] = True

                    dfs(neighbor)


        for city in range(n):
            if not visited[city]:
                visited[city] = True

                count +=1

                dfs(city)

        
        return count

        # SC -> O(N) , recursive stack frames
        # TC -> O(N * N)