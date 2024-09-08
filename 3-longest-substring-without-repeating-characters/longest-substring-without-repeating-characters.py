class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "abcabcbb" ,"abc" ,"bca","cab","abc","bc","cb"
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        longest = set()

        max_longest = 0

        i,j = 0,1

        longest.add(s[i])

        while j < len(s):
            if s[j] in longest:
                longest.remove(s[i])
                i+=1
            else:
                longest.add(s[j])
                max_longest = max(max_longest,len(longest))
                j+=1

        return max_longest

        # SC -> O(N)
        # TC -> O(N)

        