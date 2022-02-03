class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(list(set(nums))) == len(nums) else True
            