class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store = {}

        for num in nums:
            if num in store:
                return True
            
            store[num] = num

        
        return False

        # SC -> O(N)
        # TC -> O(N)
        