class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = nums[0],nums[0]

        # Check if there is cycle
        while True:
            slow = nums[slow] # [4]
            fast = nums[nums[fast]]

            if slow == fast: break

        
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        

