class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1

        most_water = 0

        while l < r:
            min_height = min(height[l],height[r])
            width = r - l
            capacity = width * min_height
            most_water = max(most_water,capacity)

            if height[r] < height[l]:
                r-=1
            else:
                l+=1
        
        return most_water

        # SC -> O(1)
        # TC -> O(N)
