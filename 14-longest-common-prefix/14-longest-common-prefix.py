class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #vertical scanning is most optimal one, will not do unnecesary comparisons like horizontal
        if not strs or len(strs) == 0:  return ""
        
        for i in range(len(strs[0])):
            c = strs[0][i]      
            
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != c:
                    return strs[0][:i]
                
        return strs[0]