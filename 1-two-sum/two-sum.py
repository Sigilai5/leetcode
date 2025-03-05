class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}

        for i in range(len(nums)):
            expect = target - nums[i] # 9 - 2 = 7, 9 - 7 = 2

            if expect in find: # 7 
                return [find.get(expect),i]
            
            find[nums[i]] = i  # {2:0}
        
    # SC -> O(N)
    # TC -> O(N)