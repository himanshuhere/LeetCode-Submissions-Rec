# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            val.append(root.val)
            inorder(root.right)
        
        val = []
        inorder(root)
        dummy = head = TreeNode(0)
        for v in val:
            head.right = TreeNode(v)
            head = head.right
        return dummy.right
            
            