#1
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        #O(m + n * k^2) where n is the number of words, m is the length of the reference string s, and k is the length of the longest string in words.
#The reason it is k^2 is because of the slice/substring operation (word[1:]) takes O(k) time

        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        print(word_dict)
        
        for char in s:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count
    
    
    
    

#Trie Woould work bt TC to same hi hai, see all word then all chars of word. ky bkar de rhe tum trie bata k kuch nhi TLE arha yha trie + dfs+map lagna hai better go for diff solution this one up above
#2
class TrieNode:
    def __init__(self):
        self.childs={}
        self.end=False
    
    def insert(self, s):
        node = self
        for c in s:
            if c not in node.childs:
                node.childs[c]=TrieNode()
            node = node.childs[c]
        node.end=True
        
    def isSub(self, s, mains):
        i=0
        j=0
        node = self
        while i< len(s):
            c=s[i]
            if node.end == True:
                return False
            if c in node.childs:
                node = node.childs[c]
                i+=1
            else:
                node = node.childs[mains[j]]
            j += 1
        return True   
                    
           
# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
#         t = TrieNode()
#         t.insert(s)
#         c=0
#         for w in words:
#             c = (c+1) if t.isSub(w, s) else c
#         return c



#1
        #i knew, TLE
#         def isSub(sub):
#             if len(sub)>len(s):
#                 return False
#             i, j = 0, 0
#             while i < len(sub) and j<len(s):
#                 if sub[i]==s[j]:
#                     i+=1
#                     j+=1
#                 else:
#                     j+=1
#                 if i==len(sub):
#                     return True
#             return i==len(sub)        
                
#         c=0
#         for sub in words:
#             if isSub(sub):
#                 c+=1
#         return c