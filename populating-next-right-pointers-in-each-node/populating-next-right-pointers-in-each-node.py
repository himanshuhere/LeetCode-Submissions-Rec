"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #easy peasy but hard on LC IB so see pepcoding video pls pls noice ques and acha 
        head = root
        while head and head.left:
            x = head
            while x:
                x.left.next = x.right
                if x.next:
                    x.right.next = x.next.left
                x = x.next
            head = head.left
        return root
        