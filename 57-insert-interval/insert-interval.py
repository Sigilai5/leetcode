class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1,3],[2,5],[6,9]] -> [[1,5],[6,9]]
        intervals.append(newInterval)

        intervals.sort(key = lambda x: x[0])

        i, j = 0, 1
        
        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:
                max_val = max(intervals[i][1],intervals[j][1])
                intervals[i][1] = max_val
                intervals.pop(j)
            else:
                i+=1
                j+=1
        

        return intervals

        # TC -> O(N Log N)
        # SC -> O(1)


        