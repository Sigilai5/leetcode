class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            sorted_word = "".join(list(sorted(word)))

            groups[sorted_word].append(word)

        
        return groups.values()

        # SC -> O(N)
        # TC -> O(N Log N)