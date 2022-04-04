# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        f = s = head
        for _ in range(k-1):
            f = f.next
        #print(f)
        for _ in range(n-k):
            s = s.next
        #print(s)
        f.val, s.val = s.val, f.val
        return head