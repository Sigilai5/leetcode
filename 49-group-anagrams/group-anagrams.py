class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for st in strs:
            sorted_st = "".join(list(sorted(st)))

            output[sorted_st].append(st)
        

        return output.values()


        # SC -> O(N)
        # TC -> O(N Log N)
        