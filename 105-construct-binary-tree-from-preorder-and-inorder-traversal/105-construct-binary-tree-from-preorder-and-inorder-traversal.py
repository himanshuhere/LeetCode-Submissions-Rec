
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {}
        for i in range(len(inorder)):
            m[inorder[i]] = i
            
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, m)
    
    #pS = pstart, Pe = pEnd, iS = istart, iE = i End, m = map
    
    def build(self, pre, pS, pE, ino, iS, iE, m):
        if pS > pE or iS > iE:  return None
        
        inRootidx = m[pre[pS]]
        leftVals = inRootidx - iS
        
        root = TreeNode(pre[pS])
        root.left = self.build(pre, pS+1, pS+leftVals, 0, iS, inRootidx-1, m)
        root.right = self.build(pre, pS+leftVals+1, pE, 0, inRootidx+1, iE, m)
        
        return root
        
    
    #2
    # if inorder:
    #         ind = inorder.index(preorder.pop(0))
    #         root = TreeNode(inorder[ind])
    #         root.left, root.right = self.buildTree(preorder, inorder[0:ind]), self.buildTree(preorder, inorder[ind+1:]) 
    #         return root
        