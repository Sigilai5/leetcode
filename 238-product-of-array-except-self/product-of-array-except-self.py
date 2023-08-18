class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [0 for i in range(len(nums))]

        prefix = 1
        for i in range(len(nums)):
            prefix_product[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1,-1):
            prefix_product[i] *= postfix
            postfix *= nums[i]
        
        return prefix_product

        # SC -> O(1)
        # TC -> O(N)
        







    







    # nums = [1,2,3,4]
    # prefix_product = [1,1,2,6]
    
    # output = [24,12,8,6]