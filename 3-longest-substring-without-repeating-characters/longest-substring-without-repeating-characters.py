class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        left,right = 0,1

        longest = 0

        unique = set()
        unique.add(s[0])
        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                right+=1
                longest = max(longest,len(unique))
            else:
                unique.remove(s[left])
                left+=1
                
        
        return longest
            

        # SC -> O(N)
        # TC -> O(N)
        