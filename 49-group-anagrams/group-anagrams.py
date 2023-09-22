class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        special = []
        if strs == [""]:
            special.append(strs)
            return special
        if len(strs) == 1:
            special.append(strs)
            return special

            

        output = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            output[sorted_word].append(word)
        
        return output.values()
        