class Solution:
    def calculate(self, s: str) -> int:
        st = []
        i = 0
        #+3+4-3*1+5/2-3
        
        s = "+" + s
        val, lsign = 0, ''        #lastSign or sign before cur val
        
        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    val = val*10 + int(s[i])
                    i += 1
                i -= 1
                
                if lsign == '+':    st.append(val)
                elif lsign == '-':  st.append(-1*val)
                elif lsign == '*':  st.append(st.pop()*val)
                elif lsign == '/':  st.append(int(st.pop()/val))
                    
            elif s[i] in '+-*/':
                lsign = s[i]
                val = 0
            
            i+=1
            
        return sum(st)
        
                