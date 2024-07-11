class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sort in descending order -> [6,5,4,3,2,1]
        # loop range k - 1 times
        # peek and a negative sign

        heap = []

        for num in nums:
            heapq.heappush(heap,-num)

        for _ in range(k-1):
            heapq.heappop(heap)

        return -heap[0]

# SC -> O(N)
# TC -> O(N Log N)

        