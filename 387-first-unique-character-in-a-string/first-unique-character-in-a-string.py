class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabet = [0 for i in range(26)]
        
        for char in s:
            alphabet[ord(char) - ord('a')]+=1

        for i in range(len(s)):
            pos = ord(s[i]) - ord('a')
            if alphabet[pos] == 1:
                return i
        
        return -1
            

        
        