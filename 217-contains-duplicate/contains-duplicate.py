class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set()

        for num in nums:
            if num in distinct:
                return True
            else:
                distinct.add(num)

        
        return False

        # SC -> O(N)
        # TC -> O(1)

        