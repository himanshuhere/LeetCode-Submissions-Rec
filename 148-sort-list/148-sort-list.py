# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        #cut the list into two halves
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        second = slow.next
        slow.next = None
        
        l = self.sortList(head)
        r = self.sortList(second)
        
        return self.merge(l, r)
    
    
    def merge(self, l, r):
        dummy = head1 = ListNode(0)
        
        while l and r:
            if l.val <= r.val:
                head1.next = l
                l = l.next
            else:
                head1.next = r
                r = r.next
                
            head1 = head1.next
            
        head1.next = l or r
        return dummy.next