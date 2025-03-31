class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l+=1
            else:
                r-=1
        
        return -1

    # SC -> O(1)
    # TC -> O(N)
        