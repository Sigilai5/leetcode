class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k_largest = k
        self.items = nums

    def add(self, val: int) -> int:
        self.items.append(val)
        self.items.sort()

        rev_items = self.items[::-1]

        return rev_items[self.k_largest - 1]


            


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)