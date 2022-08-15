# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None]*k
        
        len_ = self.length(head)
        
        part = len_//k
        distribute = len_%k
        
        res = [None]*k      #its better to do this rather append, else [[1],[2],[3],[],[]] case me last k blank reh jayege isse ye edge case cover ho jayega 
        pre = None
        cur = head
                
        i = 0
        while cur and i < k:
            res[i] = cur
            for _ in range(part):
                pre = cur
                cur = cur.next
            
            if distribute>0:
                pre = cur
                cur = cur.next
                
            pre.next = None
            distribute -= 1
            
            i += 1
        
        return res
        
    def length(self, head):
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l += 1
        return l