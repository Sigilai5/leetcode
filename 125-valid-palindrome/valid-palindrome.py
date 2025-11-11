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
        # reverse array and compare with original array
        return output == output[::-1]

        # SC -> O(N)
        # TC -> O(N)
        