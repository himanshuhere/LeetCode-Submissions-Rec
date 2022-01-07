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
        


#Reservoir sampling which is a family of randomized algorithms for sampling from a population of unknown size.