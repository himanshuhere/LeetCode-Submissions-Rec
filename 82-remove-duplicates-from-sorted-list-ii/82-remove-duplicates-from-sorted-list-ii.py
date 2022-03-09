# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #two pointer approach
        #maine likha pura LL maine kiya arrray samjh k two pointer
        
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        cur = head
        
        while cur and cur.next:
            while cur and cur.next and cur.val == cur.next.val:
                cur = cur.next
            
            if pre.next != cur:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
                
        return dummy.next