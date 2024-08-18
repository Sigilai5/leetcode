class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_id = {}

        for i in range(len(nums)):
            dif = target - nums[i]

            if dif in num_id:
                return {i,num_id.get(dif)}
            
            num_id[nums[i]] = i

# SC -> O(N)
# TC -> O(N)
        