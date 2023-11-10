class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums

        nums_count = {}

        for num in nums:
           nums_count[num] = nums_count.get(num,0)+1

        heap = []

        for key, value in nums_count.items():
            heap.append((-value,key))

        heapq.heapify(heap)

        output = []

        for _ in range(k):
            if heap:
                output.append(heapq.heappop(heap)[1])

        return output

        # SC -> O(N)
        # TC -> O(N Log K)
            
        