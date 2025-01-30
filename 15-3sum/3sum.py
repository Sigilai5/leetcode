class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i+1
            k = len(nums) - 1

            while j < k:
                if i !=j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                    unique.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while j < k and nums[j] == nums[j-1]:
                        j+=1

                    while j < k and nums[k] == nums[k+1]:
                        k-=1 

                elif i !=j and i != k and j != k and nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1

        
        return unique

        # SC -> O(1)
        # TC -> O(N*M)
                
            
        