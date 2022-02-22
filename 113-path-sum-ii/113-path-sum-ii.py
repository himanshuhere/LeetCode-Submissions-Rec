# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(root, tar, arr):
            if not root:
                return
            if not root.left and not root.right and tar == root.val:
                arr.append(root.val)
                self.res.append(arr)
                return
            
            helper(root.left, tar-root.val, arr+[root.val])
            helper(root.right, tar-root.val, arr+[root.val])
        
        self.res = []
        helper(root, targetSum, [])
        return self.res

        #TC can be n^2 at worst, n for dfs and copying array can reach n.
        #We cant make tar<0:return as there might be negative values too as per constraints
        #2 bfs
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res
        
        
    