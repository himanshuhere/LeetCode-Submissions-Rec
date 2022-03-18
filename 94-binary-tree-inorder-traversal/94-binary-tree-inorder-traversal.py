# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st, res = [], []
        while st or root:
            if root:            #Go left
                st.append(root)
                root = root.left
            else:
                root = st.pop() #pop and add val
                res.append(root.val)
                root = root.right   #go right
        return res
        
        
        def fn(root):
            if not root:
                return
            fn(root.left)
            ans.append(root.val)
            fn(root.right)
        
        ans = []
        fn(root)
        return ans