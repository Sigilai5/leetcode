class Solution:
    def isValid(self, s: str) -> bool:
        while s:
            if "()" in s:
                s = s.replace("()","")
            elif "[]" in s:
                s = s.replace("[]", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            else:
                return False
        

        return True
        
        # TC -> O(N)
        # SC -> O(N)