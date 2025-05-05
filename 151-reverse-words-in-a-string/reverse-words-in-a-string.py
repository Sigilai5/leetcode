class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        
        stack = []

        for word in s:
            stack.append(word)


        result = []

        while stack:
            result.append(stack.pop())

        return ' '.join(result)


        # SC -> O(N)
        # TC -> O(N)
    

        