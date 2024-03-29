class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

        heapq.heapify(self.nums) # [2,4,5,8]  

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val) # [2,3,4,5,8]

        while self.nums and len(self.nums) != self.k:
            heapq.heappop(self.nums)
        
        # [2,3,4]

        return self.nums[0]
        
        # SC -> O(N)
        # TC -> O(N Log K)
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)