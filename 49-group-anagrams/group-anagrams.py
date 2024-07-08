class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagram = defaultdict(list)

        for st in strs:
            sorted_st = "".join(sorted(list(st)))
            groupedAnagram[sorted_st].append(st)
        

        return groupedAnagram.values()
        
        # SC -> O(N)
        # TC -> O(N Log N)