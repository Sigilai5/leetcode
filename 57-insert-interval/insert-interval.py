class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key=lambda x:x[0])

        i = 0
        j = 1

        while j < len(intervals):
            if intervals[j][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1],intervals[j][1])
                intervals.pop(j)
            else:
                i+=1
                j+=1
        

        return intervals
        

        # SC -> O(1)
        # TC -> O(N Log N)