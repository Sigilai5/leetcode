class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        num_list = []
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
            
            num_list.append(i)
            powers[i] = steps
        

        heap = []

        for num, power in powers.items():
            heapq.heappush(heap,(power,num))

        for i in range(k-1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)[1]



    # SC -> O(N)
    # TC -> O(NLogK)



# Solutio with TC -> O(N Log N)

# class Solution:
#     def getKth(self, lo: int, hi: int, k: int) -> int:
#         num_list = []
#         powers = {}

#         for i in range(lo,hi+1):
#             power = i
#             steps = 0

#             while power != 1:
#                 if power % 2 == 0:
#                     power = power / 2
#                     steps+=1
#                 else:
#                     power = 3 * power + 1
#                     steps+=1
            
#             num_list.append(i)
#             powers[i] = steps
        

#         num_list.sort(key = lambda x:powers[x])

#         return num_list[k - 1]

    # SC -> O(N)
    # TC -> O(NLogN)

        

        