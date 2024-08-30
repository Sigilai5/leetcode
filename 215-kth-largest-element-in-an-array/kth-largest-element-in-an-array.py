class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k] # [3,2]

        heapq.heapify(min_heap)

        for num in nums[k:]: # [1,5,6,4]
            if num > min_heap[0]:
                heapq.heapreplace(min_heap,num) # [5,6]
        
        return min_heap[0]
    
    # SC -> O(N)
    # TC -> O(N Log K)