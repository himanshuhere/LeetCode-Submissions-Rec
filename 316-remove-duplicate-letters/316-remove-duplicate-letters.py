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