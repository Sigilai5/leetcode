class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        

        left,right = 0,0

        unique = set()

        max_len = 0

        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                max_len = max(max_len,len(unique))
                right+=1
            else:
                unique.remove(s[left])
                left+=1

        return max_len

        # SC -> O(N)
        # TC -> O(N)