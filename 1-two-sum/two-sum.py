class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            dif = target - nums[i]

            if dif in check:
                return [i,check.get(dif)]

            check[nums[i]] = i

        
        return [-1,-1]

        # SC -> O(N)
        # TC -> O(N)
        