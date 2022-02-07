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
        

        fast = slow = head
        for _ in range(n):          #1<=n<=size
            fast = fast.next
            
        if not fast:            #need to handle, if no dummy created for slow,fast before head
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return head
        