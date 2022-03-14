class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        st = []
        
        for p in path:
            if p == "" or p == ".":
                continue
            if p == "..":
                if st:
                    st.pop()
            else:
                st.append(p)
                
        return "/" + "/".join(st)