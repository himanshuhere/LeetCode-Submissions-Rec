class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #see strivers both sol
        #brute
        
        oldToCopy = {None : None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            oldToCopy[cur].next = oldToCopy[cur.next]   #what if cur.next is none, thus init map as None: None
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next 
            
        return oldToCopy[head]
    
    
        #optimal
        if not head:
            return 
        # copy nodes
        cur = head
        #pass 1
        while cur:
            nxt = cur.next
            cur.next = Node(cur.val)
            cur.next.next = nxt
            cur = nxt
            
        #pass 2
        # copy random pointers
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        #pass 3
        # separate two parts
        second = cur = head.next
        while cur.next:
            head.next = cur.next
            head = head.next
            cur.next = head.next
            cur = cur.next
        head.next = None
        
        return second
    
        