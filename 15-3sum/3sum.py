class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()

        for i in range(len(nums)):
            j,k = i+1, len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    output.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1
        
        return output
        

        # TC -> O(N log N) + O(N^2) = O(N^2)

        # SC -> O(N)