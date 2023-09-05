class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:x[0] - x[1])
        
        mid_point = len(costs) // 2
        initial_sum = 0

        for i in range(0,len(costs) // 2):
            initial_sum += costs[i][0]
        

        for i in range(len(costs) // 2, len(costs)):
            initial_sum += costs[i][1]
        

        return initial_sum


        # Space Complexity -> O(1)
        # Time Complexity -> O(N Log N)

        # sort by start value
        # get the mid point
        # initialize a sum of zero
        # loop through array upto len(costs) // 2
        # find sum of the first indices
        # loop through array from len(costs)//2 to the last index
        # find sum of the second indices
        