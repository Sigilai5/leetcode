class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_longest = 0
        i,j = 0, 0
        sub = set()

        while j < len(s):
            if s[j] not in sub:
                sub.add(s[j])
                max_longest = max(max_longest,len(sub))
                j+=1
            else:
                sub.remove(s[i])
                i+=1
        
        return max_longest

        # TC -> O(N)
        # SC -> O(N)

        