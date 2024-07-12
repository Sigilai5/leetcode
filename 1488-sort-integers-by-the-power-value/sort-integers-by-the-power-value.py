class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = [i for i in range(lo,hi+1)]
        
        countDict = {}

        for num in nums:
            count = 0
            val = num 

            while val != 1:
                if val%2 == 0:
                    val = val / 2
                    count+=1
                else:
                    val = 3 * val + 1
                    count+=1
                
            countDict[num] = count

        vals = [(val,key) for key,val in countDict.items()]
        
        heapq.heapify(vals)

        for _ in range(k-1):
            if vals:
                heapq.heappop(vals)

        
        return heapq.heappop(vals)[1]

    # SC -> O(N)
    # TC -> O(N Log K)