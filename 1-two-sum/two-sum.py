class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        expect = {}

        for i in range(len(nums)):
            dif = target - nums[i]

            if dif in expect:
                return [i,expect.get(dif)]
            else:
                expect[nums[i]] = i
        
        return []

        # SC -> O(N)
        # TC -> O(N)

        