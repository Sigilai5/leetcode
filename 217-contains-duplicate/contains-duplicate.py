class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set()

        for num in nums:
            if num in check:
                return True
            check.add(num)

        return False

        # SC -> O(N)
        # TC -> O(N)
        