class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1

        heap = []

        for key,val in count.items():
            heapq.heappush(heap,(-val,key))

        output = []

        for i in range(k):
            if heap:
                output.append(heapq.heappop(heap)[1])

        return output

        # SC -> O(N)
        # TC -> O(N Log N)
