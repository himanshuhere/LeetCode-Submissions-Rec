class TrieNode():
    def __init__(self):
        self.childs = {}
        self.index = -1        #very imp, for index purpose

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, i):
	    # node.index can be overwritten when a larger one is inserted, WOW
        
        node = self.root
        node.index = i
        for c in word:
            if c not in node.childs:
                node.childs[c] = TrieNode()
            node = node.childs[c]
            node.index = i
    
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.childs:
                return -1
            node = node.childs[c]
        return node.index
        
        
class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for i in range(len(words)):
            l = len(words[i])
            for j in range(l):
                self.trie.insert(words[i][j:] + '#' + words[i], i)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.search(suffix + '#' + prefix)