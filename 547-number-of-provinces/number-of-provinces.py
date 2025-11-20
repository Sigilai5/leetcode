class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected: return 0

        n = len(isConnected)

        visited = [False] * n

        count = 0


        for city in range(n):
            if not visited[city]:
                count += 1
                visited[city] = True

                queue = deque()
                queue.append(city)

                while queue:
                    current_city = queue.popleft()

                    for neighbor in range(n):
                        if isConnected[current_city][neighbor] == 1 and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

        
        return count
        

        # SC -> O(N)
        # TC -> O(N * N)