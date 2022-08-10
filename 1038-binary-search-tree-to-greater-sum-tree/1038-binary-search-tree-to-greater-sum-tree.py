#read -  every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
#read - GIVEN BST
#so do REVERSE INORDER, you ll got the lasrgest element aup smaller me pcuhe aate jaoge bas el global sum lop jo sum leta hua arha h kisi b node ,me u know mai iske sare bado se hoke arha hu sum b la rha hu
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            dfs(root.right)
            self.sum += root.val
            root.val = self.sum
            dfs(root.left)
        
        self.sum = 0
        dfs(root)
        return root