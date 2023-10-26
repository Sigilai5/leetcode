class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = defaultdict(list)

        for st in strs:
            sorted_st = "".join(sorted(st))
            output[sorted_st].append(st)



        return output.values()


        # TC -> O(NLogN)
        # SC -> O(N)
        