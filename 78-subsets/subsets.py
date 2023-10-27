class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(result,nums,subset,start):
            result.append(subset[:])

            for i in range(start,len(nums)):
                subset.append(nums[i])

                backtrack(result,nums,subset,i+1)

                subset.pop(-1)

        

        result = []
        subset = []

        nums.sort()

        backtrack(result,nums,subset,0)

        return result
        
        # TC -> O(2^N)
        # SC - O(N)
