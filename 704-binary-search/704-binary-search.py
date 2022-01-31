class Solution(object):
    def search(self, nums, target):
        return -1 if target not in nums else nums.index(target)
        