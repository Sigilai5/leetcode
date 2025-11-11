class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove empty spaces
        s = s.replace(" ","")
        # convert to lowercase
        s = s.lower()
        # create output array
        output = []
        # append letters to array
        for char in s:
            if char.isalnum():
                output.append(char)
        left,right = 0, len(output) - 1

        while left < right:
            if output[left] != output[right]:
                return False
            else:
                left +=1
                right -= 1
        

        return True
        