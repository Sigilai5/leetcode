class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

        # SC -> O(N)
        # TC -> O(N)
        