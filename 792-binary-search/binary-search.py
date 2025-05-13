class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums) - 1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target: return mid

            if nums[mid] > target: right-=1

            elif nums[mid] < target: left+=1

        
        return -1

        # TC -> O(Log N)
        # SC -> O(1)
        