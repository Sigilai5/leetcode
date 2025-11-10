class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            dif = target - nums[i]

            if dif in seen:
                return [i, seen.get(dif)]
            
            seen[nums[i]] = i

        
    
    # SC -> O(N)
    # TC -> O(N)




        