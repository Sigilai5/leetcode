class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            expect = target - nums[i]

            if expect in check:
                return [check.get(expect),i]
            
            check[nums[i]] = i
        
        return []
        
        # SC -> O(N)
        # TC -> O(N)