class Solution(object):
    def missingNumber(self, nums):
        num_range = range(0, len(nums)+1)
        for i in num_range:
            if i not in nums:
                return i