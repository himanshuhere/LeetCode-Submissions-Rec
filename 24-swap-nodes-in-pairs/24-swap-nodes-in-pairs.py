# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        
        while cur and cur.next:
            tmp = cur.next
            cur.next = tmp.next

            tmp.next = cur
            pre.next = tmp

            pre = cur
            cur = cur.next

        return dummy.next
