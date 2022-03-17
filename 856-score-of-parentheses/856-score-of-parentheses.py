class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        st.append(0)
        score = 0
        n = len(s)
        i = 0
        while i < len(s):
            if s[i] == '(':
                st.append(s[i])
                i += 1
            else:
                if st and st[-1] != '(':
                    cur = 0
                    while st and st[-1] != '(':
                        cur += st.pop()
                    if st:
                        cur *= 2
                        st.pop()
                    st.append(cur)
                    i += 1

                else:           #it will surely have values
                    opencount = 0
                    while i < n and st and s[i] == ')' and st[-1] == '(':
                        opencount += 1
                        st.pop()
                        i += 1
                    cur = st.pop() if (st and st[-1] != '(') else 0
                    cur += (pow(2, opencount-1))
                    st.append(cur)
        return sum(x for x in st if x != '(')
                    