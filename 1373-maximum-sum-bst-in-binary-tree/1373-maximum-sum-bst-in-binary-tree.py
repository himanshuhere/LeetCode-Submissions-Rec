# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def check(node):
            nonlocal res
            if not node: 
                return 0, True, -inf, inf  #sum, isBST, MIN, MAX
            
            s1, bst1, maxi1, mini1 = check(node.left)
            s2, bst2, maxi2, mini2 = check(node.right)
            
            if bst1 and bst2 and maxi1 < node.val < mini2:
                sum_ = node.val + s1 + s2       #1 insted sum, you get max size bst in BT
                res = max(res, sum_)
                return sum_, True, max(maxi2, node.val), min(node.val, mini1)
            
            return 0, False, -inf, inf
        
        res = 0
        check(root)
        return res