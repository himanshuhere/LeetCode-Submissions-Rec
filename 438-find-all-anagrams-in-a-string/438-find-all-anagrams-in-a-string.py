class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #Aditya fixed sliding window format, with very smart trick to save time while calculating len of map see
        
        map_ = Counter(p)
        k = len(p)
        count = len(map_)          #very useful variable 
        ans = []                #will have the starting index
        i, j = 0, 0
        
        while j < len(s):
            
            if s[j] in map_:
                map_[s[j]] -= 1
                if map_[s[j]] == 0:     #just now went 0, then one char lost in map
                    count -= 1
                
            if (j-i+1) == k:
                if count == 0:
                    ans.append(i)
                    
                if s[i] in map_:
                    map_[s[i]] += 1
                    if map_[s[i]] == 1:
                        count += 1
                    
                i += 1
            j+=1
        return ans
        
                        
        