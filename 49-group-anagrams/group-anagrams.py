class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for st in strs:
            anagram = [0] * 26
            for i in range(len(st)):
                anagram[ord(st[i]) - ord('a')]+=1
            anagrams[tuple(anagram)].append(st)
        
        return anagrams.values()

        # SC -> O(N)
        # TC -> O(N)
        