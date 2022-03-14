# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        
        turn = 0
        while head:
            if turn == 0:       #first
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next    
            turn ^= 1
            
        even.next = None            #very imp, was getting errors
        odd.next = dummy2.next
        return dummy1.next