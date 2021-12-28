# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sl = fs = head
        while fs and fs.next:
            sl, fs = sl.next, fs.next.next
        return sl