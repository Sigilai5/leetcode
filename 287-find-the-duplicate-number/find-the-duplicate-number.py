class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = nums[0],nums[0]

        # Check if there is a cycle by slow x1 and fast x2
        while True:
            slow = nums[slow] # [4]
            fast = nums[nums[fast]]

            if slow == fast: break

        
        slow = nums[0]

        # Check if there is a cycle by slow x1 and fast x1
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

        # SC -> O(1)
        # TC -> O(N)
        
        
