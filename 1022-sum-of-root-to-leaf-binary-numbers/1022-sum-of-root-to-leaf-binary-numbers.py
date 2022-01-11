# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root, cur):
            if not root:
                return
            if not root.left and not root.right:
                cur += str(root.val)
                self.ans += int(cur, 2)
                return
            cur += str(root.val)
            dfs(root.left, cur)
            dfs(root.right, cur)
        
        dfs(root, "")
        return self.ans
                