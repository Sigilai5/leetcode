class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = "".join(list(sorted(word)))

            anagrams[sorted_word].append(word)


        return list(anagrams.values())   

        # SC -> O(N)
        # TC -> O(N Log N)     