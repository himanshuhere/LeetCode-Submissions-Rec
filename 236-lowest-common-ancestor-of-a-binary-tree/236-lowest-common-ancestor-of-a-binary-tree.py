# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Fot BT
        if not root or root is p or root is q:
            return root
        
        l, r = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        
        if l and r:
            return root
        elif not l:
            return r
        else:
            return l
        
        
        #This code is for BST, curr ques is BT. so above will work only.
        #LCA for BST --- *****BST*****
        def lca(root, n1, n2):
            if root is None:
                return None

            # lies in left
            if(root.val > n1.val and root.val > n2):
                return lca(root.left, n1, n2)
            # lies in right
            elif(root.val < n1 and root.val < n2):
                return lca(root.right, n1, n2)
            else:
                return root
        
        #Iterative LCA ****BST*****
        def lca(root, n1, n2):
            while root:
                if root.data > n1 and root.data > n2:
                    root = root.left
                elif root.data < n1 and root.data < n2:
                    root = root.right
                else:
                    return root
            return root