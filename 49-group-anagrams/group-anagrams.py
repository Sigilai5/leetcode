class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            word_list = [0] * 26
            for i in range(len(word)):
                word_list[ord('a') - ord(word[i])]+=1
            
            anagrams[tuple(word_list)].append(word)

        return anagrams.values()

    # SC -> O(N)
    # TC - > O(N*M)

        