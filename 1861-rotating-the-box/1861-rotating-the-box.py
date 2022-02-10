class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # For each row:
        #     empty will point to the last cell that is empty. Initially empty = columns - 1.
        #     Start from last column in the row, for each column c:
        #     if current cell contains a stone, we will move it from current cell to the empty cell(which is represented by empty variable).
        #     if current cell contains an obstacle, we will change value of empty to c-1.
        
        R, C = len(box), len(box[0])
        
        for i in range(R):
            empty = C-1
            for j in range(C-1, -1, -1):
                if box[i][j] == "*":
                    empty = j-1
                    
                elif box[i][j] == "#":
                    box[i][j], box[i][empty] = box[i][empty], box[i][j]
                    empty -= 1
                    
        #return zip(*box[::-1])
        box2 = [[None]*R for _ in range(C)]
        for i in range(R):
            for j in range(C-1, -1, -1):
                box2[j][R-i-1] = box[i][j]
        return box2
                