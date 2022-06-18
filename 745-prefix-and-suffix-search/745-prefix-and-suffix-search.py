class TrieNode():
    def __init__(self):
        self.children = {}
        self.weight = -1        #very imp, for index purpose

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, i):
	    # node.weight can be overwritten when a larger one is inserted
        node = self.root
        node.weight = i
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.weight = i
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.weight
        
        
class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        i, n = 0, len(words)
        while i < n:
            l = len(words[i])
            for j in range(l + 1):
                self.trie.insert(words[i][j:l] + '#' + words[i], i)
            i += 1

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.search(suffix + '#' + prefix)