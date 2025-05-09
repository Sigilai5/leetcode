class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1: return len(s)

        # "abcabcbb"

        left,right = 0,1
        longest = set()

        max_len = 0

        longest.add(s[0]) # (a)
        while right < len(s):
            if s[right] not in longest:
                longest.add(s[right]) # (a,b)
                max_len = max(max_len,len(longest))
                right+=1
            else:
                longest.remove(s[left])
                left+=1

        
        return max_len

                
        # SC -> O(N)
        # TC -> O(N)