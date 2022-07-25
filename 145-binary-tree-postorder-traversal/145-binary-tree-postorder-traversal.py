# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Iterative, Two - stack, Do reverse Preorder and while res, put to another stack
        
        if not root:
            return None
        
        st = [root]
        st2 = []
        res = []
        while st:
            root = st.pop()
            st2.append(root.val)
            if root.left:
                st.append(root.left)
            if root.right:
                st.append(root.right)
        
        while st2:
            res.append(st2.pop())
        
        return res
        
        
        
        
        
        def fn(root):
            if not root:
                return
            
            
            fn(root.left)
            fn(root.right)
            ans.append(root.val)
        
        ans = []
        fn(root)
        return ans