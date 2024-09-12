class Solution:
    def lengthOfLongestSubstring(self, inputString: str) -> int:
        if not inputString: return 0
        
        seenCharacters = set() #a
        left = right = 0 #l = 0 r = 0
        
        maxLen = 0 # 1
        
        
        while right < len(inputString): #1
            currChar = inputString[right] #a
            
            while left <= right and currChar in seenCharacters:
                seenCharacters.remove(inputString[left])
                left += 1
                
            seenCharacters.add(currChar)
            currLen = (right - left) + 1
            maxLen =  max(maxLen, currLen) 
            right += 1
            
        return maxLen