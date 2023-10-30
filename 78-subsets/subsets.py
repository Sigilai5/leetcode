class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            subset = [lst + [num] for lst in output]
            output+= subset
            
        return output

        # SC -> O(2^N)
        # TC -> O(N*(2^N))
        