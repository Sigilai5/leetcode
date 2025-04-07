class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}

        for i in range(len(nums)):
            expect = target - nums[i]

            if expect in find:
                return [i, find.get(expect)] 
            
            find[nums[i]] = i
        