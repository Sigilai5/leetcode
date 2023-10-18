class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 and nums[0] == k:
            return nums

        count = {}

        for num in nums:
            count[num] = count.get(num,0)+1

        heap = [(-value,key) for key,value in count.items()]

        heapq.heapify(heap)

        output = []

        for _ in range(k):
            if heap:
                output.append(heapq.heappop(heap)[1])

        return output


        # TC -> O(N)
        # SC -> O(N)

        

       


        # check if length is 1 and k is 1 then return nums if true
        # initialize a dictionary
        # count the occurence of each number in the dictionary where key is      the number itself and value is the count
        # put the key values in an emmpty list
        # sort the dictionary values in descending order
        # initialize an empty list:
        # loop thorugh the list k times and append the values in the list
        