class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals

        intervals.sort(key=lambda x: x[0])

        left,right = 0,1

        while right < len(intervals):
            if intervals[right][0] <= intervals[left][1]:
                intervals[left][1] = max(intervals[right][1],intervals[left][1]) 
                intervals.pop(right)
            else:
                left+=1
                right+=1

        
        return intervals

        # SC _> O(N)
        # TC -> O(N log N)

