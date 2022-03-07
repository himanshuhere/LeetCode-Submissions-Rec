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
        x = self.stack[-1]
        self.stack.pop()
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


# class MinStack {
# 	private Node head;
        
#     public void push(int x) { //aage hi laga rhe hai node, o(1) thats why head = dono ,e
#         if (head == null) 
#             head = new Node(x, x, null);
#         else 
#             head = new Node(x, Math.min(x, head.min), head.next);
#     }
    
#     public void pop() {
#         head = head.next;
#     }
    
#     public int top() {
#         return head.val;
#     }
    
#     public int getMin() {
#         return head.min;
#     }
        
#     private class Node {
#         int val;
#         int min;
#         Node next;
            
#         private Node(int val, int min, Node next) {
#             this.val = val;
#             this.min = min;
#             this.next = next;
#         }
#     }
#}
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()