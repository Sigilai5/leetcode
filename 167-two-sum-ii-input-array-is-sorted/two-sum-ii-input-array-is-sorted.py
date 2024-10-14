class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0, len(numbers) - 1

        result = []

        while left < right:
            total = numbers[left] + numbers[right]

            if total > target:
                right-=1
            elif total < target:
                left+=1
            else:
                result.append(left+1)
                result.append(right+1)
                return result

        return [] 

        # SC -> O(1)
        # TC -> O(N)
         