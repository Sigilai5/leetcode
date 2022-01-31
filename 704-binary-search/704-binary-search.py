class Solution(object):
    def search(self, nums, target):
        return nums.index(target) if target in nums else -1
        