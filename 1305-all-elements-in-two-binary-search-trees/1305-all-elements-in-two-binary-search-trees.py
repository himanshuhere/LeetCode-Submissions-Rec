# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        #inorder
        def dfs(r):
            if not r:
                return
            
            dfs(r.left)
            res.append(r.val)
            dfs(r.right)
            
        res = []
        dfs(root1)
        dfs(root2)
        return sorted(res)
    
    #optimal wud be to use inorder and get two sorted list, then merge then in o(n) rather sorting