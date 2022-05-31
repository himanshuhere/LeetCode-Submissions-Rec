class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        #brute - generating all 2^k ( 1<<k) codes thats costly
        #logically ye bhi nk hi hai
        st = set()
        for i in range(0, len(s)-k+1):
            st.add(int(s[i:i+k], 2))
        
        for i in range(0, 2**k):
            if i not in st:
                return False
        return True
    
        
        #omptimized (will not generate all codes, rather try this) o(nk)
        
        st = set()
        codes = 1 << k            #2^k
        
        for i in range(0, len(s)-k+1):
            tmp = s[i:i+k]
            if tmp not in st:
                st.add(tmp)
                codes -= 1          #without heck yes, ofc obious
                
                if codes == 0:      #all present
                    return True
        return False