class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
 
        i = 1

        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])
                intervals.pop(i)
            else:
                i+=1
        
        return intervals

        # SC -> O(1)
        # TC ->  O(N Log N)





        