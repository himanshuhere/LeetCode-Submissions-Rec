# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #Two pointer approach pre and cur always with dummy LOL
        if not head:
            return None
        
        if not head:    return None
        
        dummy = prev = ListNode(0)
        prev.next = head
        
        while head.next:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        if head.val == val:
            prev.next = None
            
        return dummy.next