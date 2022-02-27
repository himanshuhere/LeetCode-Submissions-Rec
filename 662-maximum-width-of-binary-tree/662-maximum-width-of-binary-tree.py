# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0                #edge case 
        
        ans = 0
        q = deque([(root, 1)])         #(node, indexing)
        
        while q: 
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            #min_ind = q[0][1]
            for _ in range(len(q)):
                node, index = q.popleft()
                #index = index - min_ind
                if node.left: 
                    q.append((node.left, 2*index))      #2*i
                if node.right: 
                    q.append((node.right, 2*index+1))   #2*i+1        
        return ans 
    
    #commented lines are to save overflow in other language, as for long long skewed tree 2*i can lead to overflow if nodes can be 10^5 or something but hrer only 3000. so fine.
    #that code will reset every level line 1 2 3 n something
    