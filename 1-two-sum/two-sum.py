class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for index,num in enumerate(nums):
            dif = target - num 
            if dif in check:
                return [index, check.get(dif)]
            check[num] = index
        
        
        # SC -> O(N)
        # TC -> O(N)
        