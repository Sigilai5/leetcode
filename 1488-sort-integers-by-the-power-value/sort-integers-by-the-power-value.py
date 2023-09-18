class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        num_list = []
        powers = {}

        for x in range(lo,hi+1):
            power = x
            steps = 0

            while power != 1:
                if power % 2 == 0:
                    power = power / 2
                    steps+=1
                else:
                    power = 3 * power + 1
                    steps+=1
            
            num_list.append(x)
            powers[x] = steps
        

        num_list.sort(key = lambda x:powers[x])

        return num_list[k - 1]