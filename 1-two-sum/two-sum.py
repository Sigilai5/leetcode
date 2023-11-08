class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in num_index:
                return [i,num_index.get(dif)]
            else:
                num_index[nums[i]] = i
        
        # TC -> O(N)
        # SC -> O(N)