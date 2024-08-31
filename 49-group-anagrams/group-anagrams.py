class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            let_group = [0] * 26

            for i in range(len(word)):
                let_group[ord(word[i]) - ord('a')]+=1
            
            groups[tuple(let_group)].append(word)
        
        return groups.values()
        