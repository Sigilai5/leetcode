class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count  = {}

        # count occurence
        for num in nums:
            num_count[num] = num_count.get(num,0)+1

        
        elements = [(-val,key) for key, val in num_count.items()]

        heapq.heapify(elements)

        top = []

        for _ in range(k):
            top.append(heapq.heappop(elements)[1])
        
        return top

        # SC -> O(N)
        # TC -> O(N Log K)


        



        