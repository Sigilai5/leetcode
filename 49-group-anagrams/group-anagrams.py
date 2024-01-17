class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: return [strs]

        group = defaultdict(list)


        for st in strs:
            sorted_st = "".join(list(sorted(st)))

            group[sorted_st].append(st)
        

        return group.values()

        # SC -> O(N)
        # TC -> O(N Log N)
        