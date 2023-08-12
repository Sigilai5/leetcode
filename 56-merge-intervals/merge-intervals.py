class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x:x[0])

        output = [intervals[0]]

        pointer_1 = 0 # points at the output list
        pointer_2 = 1 # points at the intervals list

        while pointer_2 < len(intervals):
            if intervals[pointer_2][0] <= output[pointer_1][1]:
                output[pointer_1][1] = max(intervals[pointer_2][1],output[pointer_1][1])
            else:
                output.append(intervals[pointer_2])
                pointer_1+=1
            
            pointer_2+=1
        

        return output

        # SC -> O(N)
        # TC -> O(N Log N)




        
        