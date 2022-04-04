# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # intuitive wud be to go lenght and do len - n + 1, and remove node -- two pass
        # we ll do more optimized in one pass.
        #lol it is otimized, it is doing almoest same thing. kher know this for interview purpose but dont fall for this shitty trap of optimization. there is none
        
        #two pointers
        p1 = p2 = head
        for _ in range(n):          #1<=n<=size
            p1 = p1.next
            
        if not p1:            #need to handle, if no dummy created for slow,fast before head
            return p2.next
        
        while p1.next:
            p1 = p1.next
            p2 = p2.next
            
        p2.next = p2.next.next
        return head
    
    #and lets say you did this, your left/slow will be at exact node which needs to be deleted, so prev nooo? so one thing start with dummy and park slow/left at dummy so left will be always behind the target node.
    #Dummy is always use full to handle many edge cases easily
        