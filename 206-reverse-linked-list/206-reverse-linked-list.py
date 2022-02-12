# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #key:   tmp ---> cur.next ---> prev ---> cur ---> tmp .. so onn
#         pre = None
#         cur = head
#         while cur:
#             tmp = cur.next
#             cur.next = pre
#             pre = cur
#             cur = tmp
#         return pre
    
        #recursive
        def rev(head):
            if not head or not head.next:
                return head
            head1 = rev(head.next)
            
            #let me do my part or reversal
            head.next.next = head
            head.next = None
            
            return head1
        
        return rev(head)