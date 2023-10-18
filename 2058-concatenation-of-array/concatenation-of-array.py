class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums

        # TC -> O(N)
        # SC -> O(1)
        