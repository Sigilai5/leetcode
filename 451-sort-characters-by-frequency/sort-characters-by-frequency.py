class Solution:
    def frequencySort(self, s: str) -> str:
        s_count = {}

        for char in s:
            s_count[char] = s_count.get(char,0)+1
        
        heap = []

        for key,val in s_count.items():
            heapq.heappush(heap,(val,key))
        
        output = ""
        while heap:
            count, char = heapq.heappop(heap)
            output+=char * count
            
        return output[::-1]

        # TC -> O(N Log k)
        # SC -> O(N)
        

        # create a map
        # loop through s to get char and count
        # initialize a min heap
        # loop through map and append char and frequency
        # create an output string 
        # loop thorugh heap
        # append char * frequency in output string
        # return reversed output string