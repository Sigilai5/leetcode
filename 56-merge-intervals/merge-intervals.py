class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key = lambda x: x[0])
        
        output = [intervals[0]]

        pointer = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[pointer][1]:
                max_val = max(intervals[i][1],output[pointer][1])
                output[pointer][1] = max_val
            else:
                output.append(intervals[i])
                pointer+=1
        
        return output


        # TC -> O(NLogN)
        # SC -> O(N)

        