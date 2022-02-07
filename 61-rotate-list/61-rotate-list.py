# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0: return head
        
        #dont do one rotation then k times, waste of time see here
        
        last = head                 #we ll need it aage
        n = 1
        while last.next:            #last next cuz last next chaye humko bacha k rakhne ka
            last = last.next
            n += 1
        
        k = k%n
        if k == 0:  return head
        
        cur = head
        for _ in range(n-k-1):
            cur = cur.next
        
        #links
        last.next = head
        head = cur.next
        cur.next = None
        
        return head