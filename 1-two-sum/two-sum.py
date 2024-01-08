class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for index, item in enumerate(nums):
            dif = target - item
            if dif in check:
                return [check.get(dif), index]

            check[item] = index
        

        return [-1,-1]

        # SC -> O(N)
        # TC -> O(N)
        