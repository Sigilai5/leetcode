class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0

        i,j = 0, len(height) - 1

        while i < j:
            min_height = min(height[i],height[j])
            width = j - i
            
            max_area = max(max_area,min_height * width)
            
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
 
 
        return max_area
        
        # SC -> O(1)
        # TC -> O(N)