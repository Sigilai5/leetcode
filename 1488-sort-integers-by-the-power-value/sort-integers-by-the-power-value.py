class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = [i for i in range(lo,hi+1)]
        heap = []

        for num in nums:
            steps = 0
            x = num 

            while x != 1:
                if x % 2 == 0:
                    x = x / 2
                    steps+=1
                else:
                    x = 3 * x + 1
                    steps+=1
            heap.append((steps,num))

        heapq.heapify(heap)

        for i in range(k-1):
            if heap:
                heapq.heappop(heap)

        return heapq.heappop(heap)[1]

        # TC -> O(N Log K)
        # SC -> O(N)



        
       
        
        
    

       
        