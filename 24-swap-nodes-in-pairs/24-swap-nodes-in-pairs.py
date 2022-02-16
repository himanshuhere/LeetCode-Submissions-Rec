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

    #create a dummy and mark it as pre, because you need to add head to second node, then pre can be also used for next pair
    #make head as cur and tmp as cur.next
    #now just hold, reverse and attach pre to tmp
    #Now, be ready for next iteration. PRE = CUR and CUR = CUR.NEXT
    #why cur.next, becasue after reversal, cur will move ahead one step thus jump only one.
    #now there can be even nodes, then cur will stand at cur=None and for odd, there will be one at last we should leave that thus, cur.next==None ==> hence, while cur and cur.next: