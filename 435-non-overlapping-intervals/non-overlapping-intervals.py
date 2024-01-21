class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1: return 0

        intervals.sort(key = lambda x: x[1])

        end = intervals[0][1]

        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count+=1
            else:
                end = intervals[i][1]

        
        return count

        # SC -> O(1)
        # TC -> O(N Log N)

