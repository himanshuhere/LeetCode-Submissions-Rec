# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None
        if (head.next == None):
            del head
            return None
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        d = head
        mid = n//2
        while (mid > 1):
            mid -= 1
            head = head.next
  
        # Delete the middle node
        head.next = head.next.next

        return d
#         slow = fast = d = prev = head
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next.next
            
#         prev.next = prev.next.next if prev.next.next else None
#         return d
    
    
    
    #     print(n)
    #     n = n//2-1
    #     d = head
    #     while n:
    #         head = head.next
    #         n -= 1
    #     head.next = head.next.next
    #     return d