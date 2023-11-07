class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)

        while self.nums and len(self.nums) != self.k:
            heapq.heappop(self.nums)

        return self.nums[0]

        # TC -> O(N Log K)
        # SC -> O(N)
        
        


        


            


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)