class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_left = [0 for _ in range(len(nums))]
        product_right = [0 for _ in range(len(nums))]

        product_left[0] = 1

        for i in range(1,len(nums)):
            product_left[i] = nums[i-1] * product_left[i-1]
        

        product_right[len(nums) - 1] = 1

        for j in range(len(nums) - 2, -1,-1):
            product_right[j] = nums[j+1] * product_right[j+1]

        for i in range(len(nums)):
            nums[i] = product_right[i] * product_left[i]


        return nums        

        # SC -> O(N)
        # TC -> O(N)