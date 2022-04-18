# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            nonlocal head
            if not root:
                return
            inorder(root.left)
            head.right = TreeNode(root.val)
            head = head.right
            inorder(root.right)
        
        dummy = head = TreeNode(0)
        inorder(root)
        return dummy.right
            
            