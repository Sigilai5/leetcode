class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        numsCount = Counter(nums)

        for key,val in numsCount.items():
            if val == 1:
                return key
        
        return -1

        # SC -> O(N)
        # TC -> O(N)