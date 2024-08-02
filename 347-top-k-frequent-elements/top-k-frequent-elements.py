class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get count for individual num
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num,0)+1
        
        heap = []

        # use a 2D heap to store max values
        for key,val in num_count.items():
            heapq.heappush(heap,(-val,key))
        
        # create an empty array
        result = []

        # loop k  times
        for _ in range(k):
            if heap:
                result.append(heapq.heappop(heap)[1])
        

        return result

        # SC -> O(N)
        # TC -> O(N Log K)

        