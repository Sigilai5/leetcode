class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = set()

        for num in nums:
            if num in unique:
                return num
            unique.add(num)
        
        return -1

        # SC -> O(N)
        # TC -> O(N)
        