class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        left,right = 0, len(nums)-1

        while left <= right:
            mid_point = (left+right) // 2
            if nums[mid_point] == target:
                return mid_point
            elif nums[mid_point] < target:
                left+=1
            else:
                right-=1
        
        return -1
        
        # SC -> O(N)
        # TC -> O(Log N)