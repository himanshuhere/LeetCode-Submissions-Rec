# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    #Fixed Sampling - o(n) / o(n)
    def __init__(self, head: Optional[ListNode]): 
	    self.list = head
	    res = [] 
	    node = self.list
	    while node:             # Storing all the values by iterating over the LinkedList
		    res.append(node.val)
		    node = node.next  
	    self.res = res

    def getRandom(self) -> int:
        # The choices() method returns a list with the randomly selected element from the specified sequence.
        # As we want in range of 0 to n - 1
	    return random.choice(self.res)
    
    #Reservoir Sampling - o(n)/o(1)
    def __init__(self, head: ListNode):
        
        # Note that the head is guaranteed to be not null, so it contains at least one node.

        self.head = head

    def getRandom(self) -> int:
       
        # Returns a random node's value.
        
        curr = self.head
        res = 0
        index = 1
        
        while curr:
            if random.random() < (1/index):
                res = curr.val
            
            index += 1
            curr = curr.next
        
        return res

#Reservoir sampling which is a family of randomized algorithms for sampling from a population of unknown size.