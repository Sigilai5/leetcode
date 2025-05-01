class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []

        for i in range(1,(n//2) + 1): # find symmetric pairs
            res.append(i)
            res.append(-i)
        
        if n % 2 != 0:
            res.append(0)

        
        return res

    # SC -> O(N)
    # TC -> O(N)





        # 5
        # [1,-1,2,-2,0] # add zero to odd input make sure count array item is equal to n

        # 4
        # [1,-1,2,-2]
        