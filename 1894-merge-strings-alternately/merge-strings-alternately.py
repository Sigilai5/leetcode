class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        i,j = 0, 0

        while i < len(word1) and j < len(word2):
            output.append(word1[i])
            output.append(word2[j])
            i+=1
            j+=1
        

        output.append(word1[i:])
        output.append(word2[j:])


        return "".join(output)