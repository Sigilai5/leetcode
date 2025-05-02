class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True

        
        return False

    # SC -> O(1)
    # TC -> O(N Log N)        