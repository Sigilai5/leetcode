class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums

        nums_count = {}

        for num in nums:
           nums_count[num] = nums_count.get(num,0)+1

        nums_element = list(nums_count.keys())

        nums_element.sort(key=lambda x: nums_count[x],reverse=True)

        return nums_element[:k]


        # SC -> O(N)
        # TC -> O(N Log N)
            
        