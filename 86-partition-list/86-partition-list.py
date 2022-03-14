# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1 = l1 = ListNode(0)   #smaller side head and list
        h2 = l2 = ListNode(0)   #higher side head and list
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
            
        l2.next = None      #end the list
        l1.next = h2.next   #append the both smaller and higher side list
        return h1.next
    
    #it may look like we are creating and adding nodes but swear it is o(1) as 
    #on visualizing u ll get to know we are just manipulating pointers nothing more 
    #just created few nodes to start that counts as constant space
    
    #QUES. List Pivoting on k
    #SOL. - o(n)/o(1)
        less = dless = ListNode(0)
        eq = deq = ListNode(0)
        great = dgreat = ListNode(0)

        while head:
            if head.val < k:
                less.next = head
                less = less.next
            elif head.val == k:
                eq.next = head
                eq = eq.next
            else:
                great.next = head
                great = great.next
            head = head.next

        great.next = None
        eq.next = dgreat.next
        less.next = deq.next
        return dless