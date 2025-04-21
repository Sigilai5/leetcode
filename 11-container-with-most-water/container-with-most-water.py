class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1

        most_water = 0

        while l < r:
            w = r - l
            h = min(height[l],height[r])

            area = w * h
            most_water = max(most_water,area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        
        return most_water


        # SC -> O(1)
        # TC -> O(N)

        