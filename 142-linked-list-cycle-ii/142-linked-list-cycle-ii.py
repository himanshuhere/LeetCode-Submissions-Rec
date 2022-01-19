# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:   return None
        
        sl, fs = head, head
        while fs and fs.next:
            sl, fs = sl.next, fs.next.next
            if sl == fs:
                break
        
        #if not cycle
        if sl != fs:    return None
        
        #cycle
        sl = head
        while sl != fs:
            sl, fs = sl.next, fs.next
        
        return sl