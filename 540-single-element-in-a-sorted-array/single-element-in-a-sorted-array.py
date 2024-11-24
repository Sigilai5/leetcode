class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        numsCount = {}

        for num in nums:
            numsCount[num] = numsCount.get(num,0)+1

        for key,val in numsCount.items():
            if val == 1:
                return key
        
        return -1

        # SC -> O(N)
        # TC -> O(N)