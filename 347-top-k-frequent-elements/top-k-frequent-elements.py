class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k = {}

        for num in nums:
            top_k[num] = top_k.get(num,0)+1

        
        top_keys = list(top_k.keys())

        top_keys.sort(key = lambda x: top_k[x], reverse=True) 

        return top_keys[:k] 

        # SC -> O(N)
        # TC -> O(N Log N)

        
        