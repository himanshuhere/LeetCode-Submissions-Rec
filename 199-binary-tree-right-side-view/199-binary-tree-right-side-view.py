# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #reverse preorder - with level cordinate smart logic see - see copy or striver
        res = []
        
        #right side - preOrder
        def dfs(root, level):
            if not root:
                return 
            
            if level == len(res):
                res.append(root.val)
            
            if root.right:
                dfs(root.right, level+1)
            if root.left:
                dfs(root.left, level+1)
        
        def bfs(root):
            if not root:
                return None
            
            q = deque([root])
            while q:
                size = len(q)
                for i in range(size):
                    x = q.popleft()
                    if i == size-1:       #last node of this level
                        res.append(x.val)
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
            
        bfs(root)
        return res