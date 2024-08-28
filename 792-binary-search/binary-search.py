class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right-=1
            elif nums[mid] < target:
                left+=1
        

        return -1
        

# SC -> O(1)
# TC -> O(N)