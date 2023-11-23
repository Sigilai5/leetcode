class Solution:
    def maxArea(self, arr: List[int]) -> int:
        max_cap = 0 # 49
        start, end = 0, len(arr) - 1 #1 7
    
        while start < end:
            curr_cap = min(arr[start], arr[end]) * (end - start) #
            max_cap = max(max_cap, curr_cap)
            
            if arr[start] >= arr[end]:
                end -= 1
            else:
                start += 1
                
        return max_cap
            
            # SC -> O(1)
            # TC -> O(N)