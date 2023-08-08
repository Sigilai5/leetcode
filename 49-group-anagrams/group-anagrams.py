class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for char in strs:
            key = "".join(sorted(char))
            groups[key].append(char)

        

        return groups.values()

        # SC -> O(N)
        # TC -> O(NLogN)
        