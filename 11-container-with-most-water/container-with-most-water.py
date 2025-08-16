class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height) - 1

        max_water = 0


        while left < right:
            w = right - left
            h = min(height[right],height[left])

            a = w * h
            max_water = max(max_water,a)

            if height[right] < height[left]:
                right-=1
            else:
                left+=1
        
        return max_water

        # SC -> O(1)
        # TC -> O(N)
        