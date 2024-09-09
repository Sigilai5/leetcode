class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""

        if len(word1) == len(word2):
            for i in range(len(word1)):
                output+=word1[i]
                output+=word2[i]

        elif len(word1) > len(word2):
            i = 0
            while i < len(word2):
                output+=word1[i]
                output+=word2[i]
                i+=1
        
            while i < len(word1):
                output+=word1[i]
                i+=1
    
        elif len(word2) > len(word1):
            j = 0
            while j < len(word1):
                output+=word1[j]
                output+=word2[j]
                j+=1
        
            while j < len(word2):
                output+=word2[j]
                j+=1

        return output