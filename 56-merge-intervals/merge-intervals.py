class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals

        intervals.sort(key = lambda x: x[0])


        i,j = 0,1

        while j < len(intervals):
            if intervals[j][0] <=intervals[i][1]: 
                intervals[i][1] = max(intervals[i][1],intervals[j][1]) 
                intervals.pop(j)
            else:
                i+=1
                j+=1
        

        return intervals

        # TC -> O(N Log N)
        # SC -> O(1)

        
        