class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        #see saving the state, go for recursion/stack
        #recursion kinda tricky here
        #STACK STACK STACK
        
        if not head: return head
        
        dummy = Node(0)
        curr, stack = dummy, [head]
        
        while stack:
            last = stack.pop() 
            
            if last.next:
                stack.append(last.next)
            if last.child:
                stack.append(last.child)
                
            curr.next = last
            last.prev = curr  
            last.child = None       #imp as your result should be a linear linkedlist
            curr = curr.next
        
        res = dummy.next
        res.prev = None
        return res