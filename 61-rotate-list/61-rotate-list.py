# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        
        n, last = 0, head
        while last.next:
            n += 1
            last = last.next
        n += 1
        
        k = k%n
        cur = head
        k = n-k-1
        while k:
            cur = cur.next
            k -= 1
        
        last.next = head
        new = cur.next
        cur.next = None
        
        return new
        
        