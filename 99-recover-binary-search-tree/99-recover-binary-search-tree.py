# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def inorder(root, first):
            nonlocal i, f, s
            if not root:
                return
            inorder(root.left, first)
            if first:
                ino.append(root.val)
            else:
                if not f and root.val != ino[i]:
                    f = root
                elif f and root.val != ino[i]:
                    s = root
                i += 1
            inorder(root.right, first)
        
        ino = []
        inorder(root, True)
        ino.sort()
        
        i = 0
        f, s = None, None
        inorder(root, False)
        f.val, s.val = s.val, f.val
        return root