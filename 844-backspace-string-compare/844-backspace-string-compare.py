class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #you need to remove previous element when you find #, ab## but in test case like this you also need to remember previous chars thus when you get multiple # you can remove recent chars. Itne ke bad bhi nahi samjh aarha STACK use hoga brute me atleast. Buddhiheen jara soch liya karo itna
        
        def build(str):
            st = []
            for ch in str:
                if ch != "#":
                    st.append(ch)
                else:
                    if st:
                        st.pop()
                        
            return "".join(st)
        
        return build(s) == build(t)
    
    
    #O(1) space
        i, j = len(s)-1, len(t)-1
        sskip, tskip = 0, 0
        
        while i >= 0 or j >= 0: #and nhi or, s ya t chota ek bada ho sakta hai bade wale me # jada ho sab pop ho jaye isliye or
            while i >= 0:
                if s[i] == "#":
                    sskip += 1
                    i -= 1
                elif sskip > 0:
                    sskip -= 1
                    i -= 1
                else:
                    break
            
            while j >= 0:
                if t[j] == "#":
                    tskip += 1
                    j -= 1
                elif tskip > 0:
                    tskip -= 1
                    j -= 1
                else:
                    break
            
            if (i >= 0) != (j >= 0):    #esa isliye ki test case 2 chalao, dono i, j =-1 ho jayege tab b ans sahi hai na to dono false ya dono true
                return False
            
            #if two char are different
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            i -= 1
            j -= 1
        
        return True
            