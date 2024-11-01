class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDif = 0
        i,j = 0,1

        while j < len(nums):
            if nums[j] > nums[i]:
                dif = nums[j] - nums[i]
                maxDif = max(maxDif,dif)
                j+=1
            else:
                i = j
                j+=1
        

        if maxDif == 0: return -1

        return maxDif


        # SC -> O(1)
        # TC -> O(N)


        