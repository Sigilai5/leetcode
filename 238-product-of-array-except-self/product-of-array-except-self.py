class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0 for _ in range(len(nums))]
        right = [0 for _ in range(len(nums))]

        # for left
        left[0] = 1

        for i in range(1,len(nums)):
            left[i] = nums[i-1] * left[i-1]

        # for right
        right[len(nums) - 1] = 1

        for j in range(len(nums) - 2,-1,-1):
            right[j] = nums[j+1] * right[j+1] 
        
        # for result
        for i in range(len(nums)):
            nums[i] = left[i] * right[i]

        return nums

        # SC -> O(N)
        # TC -> O(N)

        