class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num,0)+1
        
        heap = []

        for num, count in nums_count.items():
            heapq.heappush(heap,(-count,num))

        output = []

      
        
        for i in range(k):
            count,num = heapq.heappop(heap)
            output.append(num)
        
        return output


        # SC -> O(N)
        # TC -> O(N Log k)


        # initialize a map
        # loop through nums and get num and count of num
        # initalize a list
        # loop through map and store num and count in tuple inside list
        # sort list by count of num,and reverse
        # initalize empty output list
        # loop through former list k times while appending num
        # return output list

        