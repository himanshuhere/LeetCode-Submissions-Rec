class Solution:
    def simplifyPath(self, path: str) -> str:
        #Whole idea is that, if we find "." so we ll jump on current directory thus, just ignore it. Do not add to valid path.
        #If "..", thus we need to jump current + previous dir, thus only because of this we need STACK, else kaam normal string se ho jana tha. Baki ignore "/////" etc.
        #bhery easzy
        
        parts = path.split("/")
        stack = []
        for p in parts:
            if p in ["", "."]:      #if more /// like this it will split in ""
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)