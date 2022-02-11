class Solution:
    def compress(self, chars: List[str]) -> int:
        #two pointer
        i, j = 0, 0
        while j < len(chars):
            curchar = chars[j]
            cnt = 0
            while j < len(chars) and chars[j] == curchar:
                cnt += 1
                j += 1
            
            chars[i] = curchar  #redundnt
            i += 1
            
            #if count is 1 (count allwyas be >= 1), dont add it else add it unit wise
            if cnt > 1: 
                for c in str(cnt):
                    chars[i] = c
                    i += 1
        
            
        return i
                
            