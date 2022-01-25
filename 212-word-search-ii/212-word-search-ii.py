#first do word search 1, thats simple brute force backtracking. doing dfs from evry indices and finding it word is present. now for a list of words applying that same algo would be not effient but this backtrack is only option we have for this. so we using Trie or Prefix tree to map all words with same prefix together and then appying same word search 1 algo, thats y go n see her i mean that problem

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:      #if not then create
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        #end
        cur.isEnd = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        res, vis = set(), set()
            
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        def dfs(i, j, node, curword):
            if i<0 or j<0 or i>=R or j>=C or board[i][j] not in node.children or (i, j) in vis:
                return
            
            
            vis.add((i,j))
            node = node.children[board[i][j]]
            curword += board[i][j]
            if node.isEnd:
                res.add(curword)
            
            
            dfs(i+1, j, node, curword)
            dfs(i, j+1, node, curword)
            dfs(i-1, j, node, curword)
            dfs(i, j-1, node, curword)
            
            vis.remove((i,j))
        
        for i in range(R):
            for j in range(C):
                dfs(i, j, root, "")
                
        return list(res)