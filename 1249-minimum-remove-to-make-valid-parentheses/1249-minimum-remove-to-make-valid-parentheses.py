class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #forward
        ans = ""
        op, cl = 0, 0
        for ch in s:
            if ch == '(':
                op+=1
            elif ch == ')':
                cl+=1
            
            if cl > op:
                cl -= 1
            else:
                ans += ch       #this is n opertation. if want use string arr to get o(1)

        #backward
        s = ans
        ans = ""
        op, cl = 0, 0
        for ch in s[::-1]:
            if ch == '(':
                cl+=1
            elif ch == ')':
                op+=1
            
            if cl > op:
                cl -= 1
            else:
                ans += ch 
                
        return ans[::-1]