class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1: return 0

        # [[1, 2], [2, 3], [3, 4], [1, 3]]
        intervals.sort(key=lambda x:x[1])
        # [[1, 2], [2, 3], [1, 3], [3, 4]]

        end = intervals[0][1]

        i = 1

        count = 0

        while i < len(intervals):
            if intervals[i][0] < end:
                count+=1
            else:
                end = intervals[i][1]
            
            i +=1
        
        return count

    # SC -> O(1)
    # TC -> O(N log N)
        