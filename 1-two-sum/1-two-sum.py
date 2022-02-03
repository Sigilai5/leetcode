class Solution(object):
    def twoSum(self, nums, target):
        index_arr = []
        original_nums = [i for i in nums]
        index_fin = []
        for i in nums:
            original_nums.remove(i)
            for j in original_nums:
                if i + j == target:
                    index_arr.append(i)
                    index_arr.append(j)
        if index_arr[0] == index_arr[1]:
            for n,i in enumerate(nums):
                if i == index_arr[0]:
                    index_fin.append(n)
        else:
            index_fin.append(nums.index(index_arr[0]))
            index_fin.append(nums.index(index_arr[1]))

        return index_fin
                    
                    
            
       
                    
                              
            
