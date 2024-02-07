class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        result = defaultdict(list)

        for st in strs:
            sorted_st = "".join(list(sorted(st)))

            result[sorted_st].append(st)
        

        return result.values()

        # SC -> O(N)
        # TC -> O(N Log N)
        