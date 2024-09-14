class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = {}

        for i in range(len(nums)):
            if nums[i] in unique and abs(unique.get(nums[i]) - i) <= k:
                return True
            
            unique[nums[i]] = i
        
        return False


# SC -> O(N)
# TC -> O(N)
       

        