class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        result = []

        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum > target:
                right-=1
            elif two_sum < target:
                left+=1
            else:
                result.append(left+1)
                result.append(right+1)
                return result
        
        return []

        # SC -> O(1)
        # TC -> O(N)


        