class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        max_length = 0
        unique = set()
        left,right = 0,0
        
        # "abcbacbb"
        
        # "abcabcbb"
        # [a,b,c]
        # [b,c]
        
        
        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                max_length = max(max_length, len(unique))
                right+=1
            else:
                unique.remove(s[left])
                left+=1
        
        return max_length

        # TC -> O(N)
        # SC -> O(N)
        