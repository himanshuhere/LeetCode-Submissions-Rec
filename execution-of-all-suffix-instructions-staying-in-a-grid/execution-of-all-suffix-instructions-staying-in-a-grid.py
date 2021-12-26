class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
    
        ans = []
        i = 0
        
        while i < len(s):
            j = i
            counter = 0
            x_axis = startPos[0]
            y_axis = startPos[1]
            
            while j < len(s):
                if s[j] == 'R':
                    y_axis += 1
                    if y_axis > n-1:
                        break
                elif s[j] == 'L':
                    y_axis -= 1
                    if y_axis < 0:
                        break
                elif s[j] == 'U':
                    x_axis -= 1
                    if x_axis < 0:
                        break
                else:
                    x_axis += 1
                    if x_axis > n-1:
                        break
                counter += 1
                j += 1
            ans.append(counter)
            i += 1
        
        return ans