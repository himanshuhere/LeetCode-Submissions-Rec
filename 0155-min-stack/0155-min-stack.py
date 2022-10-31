#Two stack
class MinStack:
    #Approach - two stack to one stack to LinkedList
    def __init__(self): #same thing u can do with LL
        self.stack = []
        self.minStack = []
    
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1] >= x:
            self.minStack.append(x)
            
    def pop(self):
        if len(self.stack) == 0:
            return
        x = self.stack.pop()
        if x == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    def getMin(self):
        if len(self.minStack) == 0:
            return -1
        return self.minStack[-1]
    
#One stack
