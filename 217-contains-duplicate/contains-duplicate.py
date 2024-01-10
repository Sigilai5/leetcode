class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hold  = set()

        for num in nums:
            if num in hold:
                return True
            else:
                hold.add(num)

        
        return False

        # SC -> O(N)
        # TC -> O(N)
        