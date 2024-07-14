class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        longest = 0

        i = 0
        j = 0

        sub = set()

        while j < len(s):
            if s[j] not in sub:
                sub.add(s[j])
                longest = max(longest,len(sub))
                j+=1
            else:
                sub.remove(s[i]) 
                i+=1
        
        return longest
    # SC -> O(N)
    # TC -> O(N)