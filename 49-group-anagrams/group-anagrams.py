# Alternate solution with time complexity of O(n*k) without sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1

            ans[tuple(count)].append(s)
                
        return ans.values()