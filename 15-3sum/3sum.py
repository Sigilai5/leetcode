class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # initialize output array/set
        output = set()
        # sort nums in ascending order
        nums.sort()
        # loop through the array nums
        for i in range(len(nums)):
            # early termination
            if nums[i] > 0:
                break

        # initialize pointer j at i + 1 and k at last index
            j,k = i + 1, len(nums) - 1 
        # use a while loop to check sum of nums[i] + nums[j] + nums[k] == 0
            while j < k:
                if (nums[i] + nums[j] + nums[k]) == 0:
        # append result in output array
                    output.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                else:
                    k-=1
        # return the array/set

        return list(output)


        # SC -> O(N)
        # TC -> O(N Log N)
        