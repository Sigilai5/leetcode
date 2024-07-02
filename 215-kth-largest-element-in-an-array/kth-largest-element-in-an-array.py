import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap,-num)

        n = 0

        while n < k - 1:
            heapq.heappop(heap)
            n+=1

        
        return -heapq.heappop(heap)