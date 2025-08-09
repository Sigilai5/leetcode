class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            sorted_word = "".join(list(sorted(word)))

            group[sorted_word].append(word)


        return list(group.values())      


        # TC -> O(N Log N)
        # SC -> O(N)  