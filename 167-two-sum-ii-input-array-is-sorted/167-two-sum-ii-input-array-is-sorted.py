class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        n = len(numbers)
        r = n - 1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1,r+ 1]
            elif sum < target:
                l+=1
            else:
                r-=1
        return [-1,-1]
       
        