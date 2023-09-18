class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = {}

        for i in range(lo,hi+1):
            power = i
            steps = 0

            while power != 1:
                if power % 2 == 0:
                    power = power / 2
                    steps+=1
                else:
                    power = 3 * power + 1
                    steps+=1
            
            powers[i] = steps
        

        heap = [(power, num) for num,power in powers.items()]
        heapq.heapify(heap)

        # for num, power in powers.items():
        #     heapq.heappush(heap,(power,num))

        for i in range(k-1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)[1]