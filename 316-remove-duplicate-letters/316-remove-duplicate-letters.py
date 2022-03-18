class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = [-1]*26
        seen = [False]*26
        
        for i in range(len(s)):
            last_idx[ord(s[i])-ord('a')] = i          #update the last occurance of every char in s

        st = []
        for i in range(len(s)):
            ch = s[i]
            if seen[ord(ch)-ord('a')]:    
                continue
            while st and st[-1] > ch and last_idx[ord(st[-1])-ord('a')] > i:
                popped = st.pop()
                seen[ord(popped)-ord('a')] = False

            st.append(ch)
            seen[ord(ch)-ord('a')] = True

        return ''.join(st)
    
#     "now try to add "b" in the stack and mark it as true, for this since the current_element("b") is less than
# the peek(top) element of stack("d")so we should pop the "d" for now and push "b" in stack but before 
# poping "d" check is there "d" is again persent in given string after this "b" , since "d" is not more 
# persent after this "b" so we can't do that pop and push operation for "d" and "b" respectively , simply 
# add "b" into the stack and mark is as true that's set, but in some case if "d" is available again after 
# that "b" then we will definitely be poping "d" from the stack and adding "b" into the stack( we can take 
# example for this case as "cbadcbcd" and try to dry run it )