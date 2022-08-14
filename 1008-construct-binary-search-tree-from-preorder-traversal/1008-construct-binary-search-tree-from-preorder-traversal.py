class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        return self.construct(preorder, 0, len(preorder)-1)
    
    def construct(self, preorder, l, r):
        if l > r:
            return None
        if l == r:
            return TreeNode(preorder[l])
        
        root = TreeNode(preorder[l])
        i = l+1
        
        while i <= r and preorder[i] < root.val:
            i += 1
    
        root.left = self.construct(preorder, l+1, i-1)
        root.right = self.construct(preorder, i, r)     #r or i + (r-i)
        
        return root