# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        #Easiest Problem of LeetCode
        
        if not node.next: node = None
            
        node.val = node.next.val
        node.next = node.next.next
        
        
        
        
        
        #It is guaranteed that the node to be deleted is not a tail node in the list.

        #in case this guarantee doesnt come with ques then we can add edge case
        #see fist line of code