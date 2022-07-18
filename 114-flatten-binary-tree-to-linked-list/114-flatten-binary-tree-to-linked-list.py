# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                #switch left to right, after holding right in tmp
                temp = cur.right
                cur.right = cur.left
                cur.left = None
                
                #append prior right to right of biggest in left subtree
                head = cur
                while head.right:
                    head = head.right
                
                head.right = temp
                
            
            cur = cur.right