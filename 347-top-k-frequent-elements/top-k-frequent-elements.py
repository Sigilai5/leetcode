class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) <= 1: return nums

        top_k = {}

        for num in nums:
            top_k[num] = top_k.get(num,0)+1

        
        heap = []

        for num,count in top_k.items():
            heapq.heappush(heap,(-count,num))
        

        output = []

        for i in range(k):
            if heap:
                output.append(heapq.heappop(heap)[1])
                

        return output

        # SC -> O(N)
        # TC ->  O(N Log K)



        
        