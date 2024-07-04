class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            num = target - nums[i]

            if num in check:
                return {i,check.get(num)}
            
            check[nums[i]] = i
        
        return []

        # SC -> O(N)
        # TC -> O(N)
        