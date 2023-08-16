class Solution:
    def repeatedCharacter(self, s: str) -> str:
        unique = set()

        for char in s:
            if char in unique:
                return char
            
            unique.add(char)