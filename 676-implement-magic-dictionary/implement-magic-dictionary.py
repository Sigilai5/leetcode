class MagicDictionary:

    def __init__(self):
        self.words = [] 
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words.append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) == len(searchWord):
                count = 0
                for i in range(len(word)):
                    if word[i] != searchWord[i]:
                        count+=1
                
                if count == 1: return True
        
        return False

        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)