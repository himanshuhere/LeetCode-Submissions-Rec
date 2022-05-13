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
        #bfs - o(n) - o(n) - ust read easy to understand
#         if root == None: return root
#         q = deque([root])
#         while q:
#             prev = TreeNode(0)
#             for _ in range(len(q)):
#                 cur = q.popleft()
#                 prev.next = cur        #every level first node ka prev is prev, a kinda dummy
#                 prev = prev.next
                
#                 if cur.left != None:
#                     q.append(cur.left)
#                 if cur.right != None:
#                     q.append(cur.right)
#         return root

    
    #2 o(n) - o(1)
        node = root
        while node:
            curr = dummy = Node(0)
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next   #next level
               
        return root