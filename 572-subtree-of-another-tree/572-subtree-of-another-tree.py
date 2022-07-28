#can also be done using euler route. anyways
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSame(self, r1, r2):
        if not r1 or not r2:
            return r1 == r2
        return r1.val == r2.val and self.isSame(r1.left, r2.left) and self.isSame(r1.right,r2.right)
        
        
            