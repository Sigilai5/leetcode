class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x: x[0] - x[1])

        total = 0
        mid_point = len(costs) // 2

        for i in range(mid_point):
            total += costs[i][0]
            total += costs[i+mid_point][1]

        return total

        # SC -> O(1)
        # TC -> O(N Log N)

        