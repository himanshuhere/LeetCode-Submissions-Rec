class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        for i in range(0, len(s)-k+1):
            st.add(int(s[i:i+k], 2))
        
        
        for i in range(0, 2**k):
            if i not in st:
                return False
        return True