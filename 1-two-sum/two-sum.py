class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in two_sum:
                return {two_sum.get(dif),i}
            
            two_sum[nums[i]] = i

        
        return -1
        

        # SC -> O(N)
        # TC -> O(N)