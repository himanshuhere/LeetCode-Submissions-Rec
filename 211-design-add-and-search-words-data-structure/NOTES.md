class TrieNode:
self.childs = {}
self.end = False
​
class WordDictionary:   #Trie
​
def __init__(self):
self.childs = {}
self.end = False
#self.root = TrieNode()
def addWord(self, word: str) -> None:
for ch in word:
if ch not in self.childs:
self.childs[ch] = WordDictionary()
self = self.childs[ch]
self.end = True
​
def search(self, word: str) -> bool:
for i, ch in enumerate(word):
if ch == ".":
for c in self.childs:
if self.search(c+word[i+1:]):
return True
return False
if ch not in self.childs:
return False
self = self.childs[ch]
return self.end
​
​
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)