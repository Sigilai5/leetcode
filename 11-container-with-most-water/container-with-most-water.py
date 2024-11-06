class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height) - 1

        mostWater = 0

        while i < j:
            h = min(height[i],height[j])
            w = j - i
            total = w * h
            mostWater = max(mostWater,total)

            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        
        return mostWater

        # SC -> O(1)
        # TC -> O(N)
        