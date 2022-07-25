# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #see copy notes - tree striver
        verticals = defaultdict(list)
        queue = deque([(root, 0, 0)]) # node, x, y
        
        while queue:
            for i in range(len(queue)):
                node, x, y = queue.popleft()
                verticals[x].append((y, node.val))
                
                if node.left:
                    queue.append((node.left, x-1, y+1)) #
                if node.right:
                    queue.append((node.right, x+1, y+1))
            
        output = []
        for x in sorted(verticals.keys()):
            column = [i[1] for i in sorted(verticals[x])]
            output.append(column)
        
        return output