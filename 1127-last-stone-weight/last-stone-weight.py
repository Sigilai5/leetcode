class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones: return 0
        if len(stones) == 1: return stones[0]

        heap = []

        for stone in stones:
            heapq.heappush(heap,-stone)

        while len(heap) != 1:
            heapq.heappush(heap,heapq.heappop(heap) - heapq.heappop(heap))
        
        return -heapq.heappop(heap)

        # SC -> O(N)
        # TC -> O(N Log N)
        



