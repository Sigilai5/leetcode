class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target: return 0
        left,right = 0,len(nums) - 1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left+=1
            else:
                right-=1
        
        return -1
        