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
            
            dfs(root.right, level+1)
            dfs(root.left, level+1)
        
        def bfs(root):
            if not root:
                return None
            
            q = deque([root])
            while q:
                size = len(q) #this is imp, kuki len(q) kahi b use karna sahinhi hai size change hota h uska
                for i in range(size):
                    x = q.popleft()
                    if i == size-1:       #last node of this level
                        res.append(x.val)
                    if x.left:
                        q.append(x.left)
                    if x.right:
                        q.append(x.right)
        
        dfs(root, 0)
        #bfs(root)
        return res
    
    
    #see, bfs me i==n-1 ki jagah i==0 kar dete aur rifhr pehle left child bad me dalte to bhi chalta.
    #bfs me same isi tarah ulta karke left view b ho jata