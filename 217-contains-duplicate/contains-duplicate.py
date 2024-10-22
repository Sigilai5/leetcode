class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

        # SC -> O(N)
        # TC -> O(N)

        
        