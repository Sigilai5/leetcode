class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = defaultdict(list)

        for word in strs:
            sorted_word = "".join(list(sorted(word)))

            unique[sorted_word].append(word)
        

        return unique.values()

        # SC -> O(N)
        # TC -> O(N * MlogM)
        