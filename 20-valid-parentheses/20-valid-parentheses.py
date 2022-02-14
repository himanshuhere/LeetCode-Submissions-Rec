class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', '}':'{',']':'['}
        stack = []
        
        for i in s:
            if i in closeToOpen:  # 1
                if stack and stack[-1] == closeToOpen[i]:   #1
                    stack.pop()
                else:
                    return False            #2
            else:
                stack.append(i)
            
        return len(stack) == 0          # 3