class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0

        unique = set()

        max_count = 0

        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                max_count = max(max_count,len(unique))
                right+=1
            else:
                unique.remove(s[left])
                left+=1

        return max_count

        # SC -> O(N)
        # TC -> O(N)
        