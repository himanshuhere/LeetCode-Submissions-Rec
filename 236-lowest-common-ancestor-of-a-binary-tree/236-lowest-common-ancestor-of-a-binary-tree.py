# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        
        l, r = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        
        if l is None:
            return r
        elif r is None:
            return l
        else:
            return root
        
        #LCA for BST --- *****BST*****
        def lca(root, n1, n2):
            # Base Case
            if root is None:
                return None

            # If both n1 and n2 are smaller than root, then LCA
            # lies in left
            if(root.data > n1 and root.data > n2):
                return lca(root.left, n1, n2)

            # If both n1 and n2 are greater than root, then LCA
            # lies in right
            if(root.data < n1 and root.data < n2):
                return lca(root.right, n1, n2)

            return root
        #Iterative LCA ****BST*****
        def lca(root, n1, n2):
            while root:
                # If both n1 and n2 are smaller than root,
                # then LCA lies in left
                if root.data > n1 and root.data > n2:
                    root = root.left

                # If both n1 and n2 are greater than root,
                # then LCA lies in right
                elif root.data < n1 and root.data < n2:
                    root = root.right

                else:
                    break

            return root