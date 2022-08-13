class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #if not s or not words or len(s) == 0 or len(words) == 0:    return []
        # wordBag = Counter(words)   # count the freq of each word
        # wordLen, numWords = len(words[0]), len(words)
        # totalLen, res = wordLen*numWords, []
        # for i in range(len(s)-totalLen+1):   # scan through s
        #     # For each i, determine if s[i:i+totalLen] is valid
        #     seen = defaultdict(int)   # reset for each i
        #     for j in range(i, i+totalLen, wordLen):
        #         currWord = s[j:j+wordLen]
        #         if currWord in wordBag:
        #             seen[currWord] += 1
        #             if seen[currWord] > wordBag[currWord]:
        #                 break
        #         else:   # if not in wordBag
        #             break    
        #     if seen == wordBag:
        #         res.append(i)   # store result
        # return res
        
        
        
        lmap = collections.Counter(words)
        k = len(words[0])
        n = len(words)
        
        res = []
        
        for i in range(0, len(s) - n*k+1):
            seen = {}
            
            for j in range(n):
                wordindex = i + j*k
                word = s[wordindex: wordindex + k]
                
                if word not in lmap:
                    break
                
                seen[word] = seen.get(word, 0) + 1
                
                if seen[word] > lmap[word]: 
                    break
                    
                if j + 1 == n:
                    res.append(i)
        
        return res