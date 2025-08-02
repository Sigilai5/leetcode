class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # BREADTH FIRST SEARCH

        if not isConnected: return 0

        n = len(isConnected)

        provinces = 0

        visited = [False] * n

        for city in range(n):
            if not visited[city]:
                visited[city] = True
                provinces+=1

                queue = deque()

                queue.append(city)


                while queue:
                    node = queue.popleft()

                    for neighbor in range(n):
                        if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

        return provinces

            
        # SC -> O(N)
        # TC -> O(N)