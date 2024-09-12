class Solution:
    def groupAnagrams(self, anagrams: List[str]) -> List[List[str]]:
        anagramsGroup = defaultdict(list)
        
        for word in anagrams:
            alphabet_positions = [0] * 26
            for i in range(len(word)):
                alphabet_positions[ord('a') - ord(word[i])]+=1 # i = b 
                
            anagramsGroup[tuple(alphabet_positions)].append(word)
        
        return anagramsGroup.values()


        # SC -> O(N)
        # TC -> O(N * M)
        