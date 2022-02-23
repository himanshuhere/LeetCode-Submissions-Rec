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