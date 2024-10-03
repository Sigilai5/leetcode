class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for i in range(len(nums)):
            dif = target - nums[i]

            if dif in check:
                return {check.get(dif),i}

            check[nums[i]] = i        


    # SC -> O(N)
    # TC -> O(N)