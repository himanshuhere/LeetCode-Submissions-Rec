# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                #switch left to right, after holding right in tmp
                temp = cur.right
                cur.right = cur.left
                cur.left = None
                
                #append prior right to right of biggest in left subtree
                head = cur
                while head.right:
                    head = head.right
                
                head.right = temp
                
            
            cur = cur.right
            
        
    #Q. Make binary tree to doubly linkedlist (inorder - inplace)
    
    def f(root, prev, head):
        if not root:
            return
        
        f(root.left)
        
        if head == None:
            head = root         #first node
        else:
            root.prev = prev
            prev.next = root
        prev = root             #keep this prev updated
        
        f(root.right)
    
    head = prev = None
    #f(root, prev, head)
    #return head

    #same algo could be used if iterative asked