class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        # SC -> O(1)
        # TC -> O(N)
        

        return -1
        