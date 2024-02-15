class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = [i for i in range(lo,hi+1)]

        count = {}

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
            count[num] = steps
        
        nums.sort(key = lambda x: count[x])

    
        return nums[k-1]

        # TC -> O(N Logn N)
        # SC -> O(N)
            
        