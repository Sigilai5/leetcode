class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.end_word = True 
        

    def search(self, word: str) -> bool:
        def backtrack(node,index):
            if index == len(word):
                return node.end_word
                 
            if word[index] == ".":
                for child in node.children.values():
                    if backtrack(child,index+1):
                        return backtrack(child,index+1)

            
            if word[index] not in node.children:
                return False
            
            return backtrack(node.children[word[index]],index+1)
            
        return backtrack(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)