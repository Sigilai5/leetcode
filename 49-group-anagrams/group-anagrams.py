class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for st in strs:
            gram = [0] * 26

            for char in st:
                gram[ord(char) - ord('a')]+=1
            
            count[tuple(gram)].append(st)
        
        return count.values()

        # SC -> O(N)
        # TC -> O(N*M)
        