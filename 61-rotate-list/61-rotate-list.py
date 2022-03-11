# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        
        #1 - O(n+(k%n))
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
        head = cur.next
        cur.next = None
        return head
    
    
        #2 - O(k + n-k) - O(n) - TLE - if not allowed % mod or lenght cal then
        sl, fs = head, head
        for i in range(k):          #you cannot mod, so whole k in circle
            fs = fs.next if fs.next else head
        
        while fs.next:
            sl = sl.next
            fs = fs.next
        
        fs.next = head
        head = sl.next
        sl.next = None
        return head
        