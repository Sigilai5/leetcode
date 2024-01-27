class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0

        i,j = 0, len(height) - 1

        while i < j:
            min_height = min(height[i],height[j])
            width = j - i
            area = min_height  * width
            max_val = max(area,max_val)

            if height[i] > height[j]: 
                j-=1
            else:
                i+=1
        

        return max_val
        

        # TC -> O(N)
        # SC -> O(1)