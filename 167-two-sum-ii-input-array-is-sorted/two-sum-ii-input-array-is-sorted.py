class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers) - 1

        while i < j:
            total_sum = numbers[i] + numbers[j]
            if total_sum > target:
                j-=1
            elif total_sum < target:
                i+=1
            else:
                return [i+1,j+1]
        
        return [1,2]


    # SC -> O(1)
    # TC -> O(N)
        