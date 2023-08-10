class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for i in range(len(nums)):
            expect = target - nums[i]
            if expect in num_index:
                return [i,num_index[expect]]
            else:
                num_index[nums[i]] = i