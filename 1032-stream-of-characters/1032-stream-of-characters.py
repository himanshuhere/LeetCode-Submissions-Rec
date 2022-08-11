
class Trie():
    def __init__(self):
        self.children = {}
        self.isEnd = False       
    
    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.isEnd = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.letters = []
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])
        
    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        #ulta check karna h
        i = len(self.letters) - 1
        
        node = self.trie
        while i >= 0:
            if self.letters[i] not in node.children:
                return False
            node = node.children[self.letters[i]]
            if node.isEnd:
                return True
            i -= 1
        return False