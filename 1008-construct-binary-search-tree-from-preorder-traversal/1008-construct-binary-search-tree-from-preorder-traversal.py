class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        return self.construct(preorder, 0, len(preorder))
    
    def construct(self, preorder, l, r):
        if l >= r:
            return None
        
        root = TreeNode(preorder[l])
        i = l+1
        
        while(i < r and preorder[i] < root.val):
            i += 1
    
        root.left = self.construct(preorder, l+1, i)
        root.right = self.construct(preorder, i, i + (r-i))
        
        return root