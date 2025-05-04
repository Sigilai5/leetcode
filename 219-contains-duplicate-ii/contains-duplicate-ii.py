class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = {}

        for i, num in enumerate(nums):
            if num in duplicates and abs(i - duplicates.get(num)) <= k:
                return True
            duplicates[num] = i
        
        return False

        # SC -> O(N)
        # TC -> O(N)
        