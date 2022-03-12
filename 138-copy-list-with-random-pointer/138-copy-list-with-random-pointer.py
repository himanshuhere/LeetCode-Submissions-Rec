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
            oldToCopy[cur].next = oldToCopy[cur.next] #what if cur.next is none, thus init map as None: None
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next 
            
        #two traversal lagege hi, else connection kispe karoge. 
        return oldToCopy[head]
    
    
    
    
    #wow. asal nodes k bich me copys bana do. Ab pehle randoms connect kardo because next karne gye to link tut jayegi and u wont b able to connect randome then so pehle random then next, while next list ll be break down into two, good return
    #Old List: A --> B --> C --> D
    #InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
    
        #2 optimal constant space
        if not head:
            return 
        
        # copy nodes
        cur = head
        #pass 1
        while cur:
            nxt = cur.next
            copy = Node(cur.val)
            cur.next = copy
            copy.next = nxt
            cur = nxt           #move
            
        #pass 2
        # copy/handling RANDOM pointers
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        #pass 3
        # separate two parts and handling ONLY NEXT
        secondHead = head.next      #to return
        
        head1 = head
        head2 = head.next
        while head2.next:
            head1.next = head2.next
            head2.next = head1.next.next
            head1 = head1.next
            head2 = head2.next
        head1.next = None       #not needed actually, but still good practice
        
        return secondHead
    
        