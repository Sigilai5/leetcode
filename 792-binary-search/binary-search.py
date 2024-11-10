class Solution:
    def search(self, nums: List[int], target: int) -> int:
        midPoint = 0
        l,r = 0,len(nums) - 1

        while l <= r:
            midPoint = (r+l)//2

            if nums[midPoint] == target:
                return midPoint
            elif nums[midPoint] > target:
                r-=1
            else:
                l+=1
        
        return -1
    
    # SC -> O(1)
    # TC -> O(Log N)