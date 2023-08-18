class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)  # [1,1,1,1]

      
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1] # 
            
        
        prod_right = 1
        for i in range(len(nums) -1, -1, -1):
            ans[i] *= prod_right
            prod_right *= nums[i]
        

        return ans
    
        # SC -> O(1)
        # TC -> O(N)



        