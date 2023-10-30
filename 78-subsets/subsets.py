class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            subset = [lst + [num] for lst in output]
            print(subset)
            output+= subset
            
        return output
        