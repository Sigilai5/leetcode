class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1
        

        heap = []

        for key,val in count.items():
            heapq.heappush(heap,(-val,key))

        result = []
        
        for _ in range(k):
            if heap:
                result.append(heapq.heappop(heap)[1])
        
        return result

        # SC -> O(N + M)
        # TC -> O(N Log N)
         