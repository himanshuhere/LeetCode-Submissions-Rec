# class MinStack:
#     #Approach - two stack to one stack to LinkedList
        
#     def __init__(self): #same thing u can do with LL
#         self.stack = []
#         self.minStack = []
    
#     def push(self, x):
#         self.stack.append(x)
#         if len(self.minStack) == 0 or self.minStack[-1] >= x:
#             self.minStack.append(x)
            

#     def pop(self):
#         if len(self.stack) == 0:
#             return
#         x = self.stack[-1]
#         self.stack.pop()
#         if x == self.minStack[-1]:
#             self.minStack.pop()

#     def top(self):
#         if len(self.stack) == 0:
#             return -1
#         return self.stack[-1]

#     def getMin(self):
#         if len(self.minStack) == 0:
#             return -1
#         return self.minStack[-1]

class MinStack:
#One stack - ghante ka kam space woi kaam ek stack me hora same space almost khair
#Whole idea is to maintian first and second min next to each other in stack. whenvr new val is min than mininmum then this will be second min and new will be first, so puch already having min then push val given. This way you always have second min after min in stack. Lets say you pop it turn out to be min only, so you can make one more pop and you get the new min update. Do one test will clear
    #Approach - two stack to one stack to LinkedList
        
    def __init__(self): #same thing u can do with LL
        self.st = []
        self.mn = math.inf
    
    def push(self, x):
        if x <= self.mn:
            self.st.append(self.mn)
            self.mn = x
        self.st.append(x)
            

    def pop(self):
        if self.mn == self.st.pop():
            self.mn = self.st.pop()
        
    def top(self):
        return self.st[-1]
    
    def getMin(self):
        return self.mn
#Linked List
# class Node:
#     def __init__(self, val, mn, nxt):
#         self.val = val
#         self.mn = mn
#         self.next = nxt
        
# class MinStack:
#     #Approach - two stack to one stack to LinkedList
#     def __init__(self):
#         self.head = None
    
#     def push(self, x):
#         if not self.head:
#             self.head = Node(x, x, None)
#         else:
#             self.head = Node(x, min(x, self.head.mn), self.head)
            
#     def pop(self):
#         self.head = self.head.next

#     def top(self):
#         return self.head.val

#     def getMin(self):
#         return self.head.mn
