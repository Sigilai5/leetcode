class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "*":
                stack.append(char)
            else:
                stack.append(char)
                for i in range(2):
                    stack.pop()
            

        output = ""

        while stack:
            output+=stack.pop()

        
        return output[::-1]

        # TC -> O(N)
        # SC -> O(N)


        # initialize a stack
        # loop through the string
        # if char is not * append to the stack
        # otherwise append char and pop twice
        # create an outupt string
        # use a while loop to pop stack until its empty
        # return output
        