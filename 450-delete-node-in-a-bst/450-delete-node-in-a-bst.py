# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #TC = O(H) = o(logn)
        #i wrote in one run
        if not root:    return root
        
        def rightMost(root):
            if not root.right:  return root
            return rightMost(root.right)
        
        def helper(root):
            if not root.left:   return root.right   #if both null right will return null cool
            if not root.right:  return root.left
            
            rightChild = root.right
            lastRightOfLeft = rightMost(root.left)
            lastRightOfLeft.right = rightChild
            
            return root.left
        
        
    #two ways: cut the right sub and append to the right of max of left sub and return left sub finally, else 2 way: cut the left and append to the left of min of right sub and return right child
    
        if root.val == key: return helper(root)
        
        dummy = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = helper(root.right)
                    break
                else:
                    root = root.right
        return dummy