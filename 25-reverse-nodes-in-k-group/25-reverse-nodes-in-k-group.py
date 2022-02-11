# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 1: return head

        dummy = ListNode(-1)
        dummy.next = head
        
        pre = curr = nex = dummy
        count = 0
        
        #calculate lenght of list
        while curr.next: 
            curr = curr.next
            count += 1
        
        #outer iteration for windows
        while count >= k:
            #curr should be at first ele in each window and nex wud be curr.next thus 
            curr = pre.next
            nex = curr.next
            
            #iteration of window itself till k - 1
            for _ in range(k-1):        #yes bcs we need to do k-1 operation of reversal for k nodes
                curr.next = nex.next
                nex.next = pre.next         #onwards 2nd iter curr wud be not same as prev-next
                
                pre.next = nex
                nex = curr.next
            
            #since curr pehla tha window ka but after rev last hogya to pre = curr thius pre.next wud be next curr for new window right
            pre = curr
            
            count -= k          #remove the window size done from count
        
        return dummy.next
            