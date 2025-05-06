class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        nums.sort()

        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1

            while j < k:
                if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                    result.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif i != j and i != k and j != k and nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1
        
        return list(result)

    # SC -> O(N)
    # TC -> O(N)
        