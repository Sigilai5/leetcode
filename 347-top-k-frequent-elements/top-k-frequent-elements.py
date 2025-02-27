class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num,0)+1

        heap = []

        for key,val in num_count.items():
            heapq.heappush(heap,(-val,key))

        result = []

        for _ in range(k):
            if heap:
                result.append(heapq.heappop(heap)[1])
        
        return result

        