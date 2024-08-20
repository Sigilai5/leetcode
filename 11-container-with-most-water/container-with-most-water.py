class Solution:
    def maxArea(self, height: List[int]) -> int:
        mostWater = 0

        left,right = 0,len(height) - 1

        while left < right:
            w = right - left
            h = min(height[left],height[right])

            mostWater = max(mostWater,w*h)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        

        return mostWater

# SC -> O(1)
# TC -> O(N)