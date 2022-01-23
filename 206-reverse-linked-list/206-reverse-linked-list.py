# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next            
            curr.next = prev
            prev = curr            
            curr = temp
        return prev
    
        #recursive
        if not head:
            return head
        
        def reverse(node):
            if (node.next == None):
                return node

            node1 = reverse(node.next)
            node.next.next = node
            node.next = None
            return node1
            
        return reverse(head)