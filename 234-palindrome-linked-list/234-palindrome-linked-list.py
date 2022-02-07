# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:        
        #More smart approach
        
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # reverse the second half
        prev = None
        curr = slow
        while curr:
            temp = curr.next            
            curr.next = prev
            prev = curr            
            curr = temp
        head1 = prev
            
        # compare the first and second half nodes
        while head1: # while head1 and head:
            if head1.val != head.val:
                return False
            head1 = head1.next
            head = head.next
            
        return True
