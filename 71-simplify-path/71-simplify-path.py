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

    
    #Whole idea is that, if we find "." so we ll jump on current directory thus, just ignore it. Do not add to valid path. and split /// will result in "" thus ignore these too
    #If "..", thus we need to jump current + previous dir, thus only because of this we need STACK, else kaam normal string se ho jana tha. Baki ignore "/////" etc.
        #bhery easzy
        #ONLY Thing needs to handle is .. else baki flow hai sidha l to r