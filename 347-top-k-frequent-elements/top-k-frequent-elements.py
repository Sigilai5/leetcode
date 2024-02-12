class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 and k == 1:
            return nums
        
        top_k = {}

        # O(N)
        for num in nums:
            top_k[num] = top_k.get(num,0)+1  

        heap = []

        # O(N)
        for key,value in top_k.items():
            heap.append((-value,key)) 

        # O(Log N)
        heapq.heapify(heap)

        result = []

        for _ in range(k):
            if heap:
                result.append(heapq.heappop(heap)[1])

        return result

        # SC -> O(N)
        # O(n + k * log(n))

        