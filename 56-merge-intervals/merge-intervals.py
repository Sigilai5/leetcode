class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals

        intervals.sort(key=lambda x: x[0])

        output = [intervals[0]] # [[1,3]]

        i = 0
        j = 1

        while j < len(intervals):
            if intervals[j][0] <= output[i][1]: # 2 <= 3
                max_sec = max(intervals[j][1],intervals[i][1])
                output[i][1] = max_sec
                intervals.pop(j)
            else:
                output.append(intervals[j])
                i+=1
                j+=1
        
        return output

        # SC -> O(N)
        # TC -> O(N Log N)


        