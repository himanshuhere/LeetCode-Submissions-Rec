class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(w1, w2):
            i = 0
            while i < len(w1) and i < len(w2) and w1[i] == w2[i]:
                i += 1
            
            if i == len(w1):    return True
            if i == len(w2):  return False    #w1 ends. still w2 has letters, not good
            return order.index(w1[i]) < order.index(w2[i])
        
        for i in range(len(words)-1):
            if not compare(words[i], words[i+1]):
                return False
        return True
            