# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        m = defaultdict(TreeNode)
        childs = set()
        
        for par, child, isleft in descriptions:
            if par in m:
                node = m[par]
            else:
                node = TreeNode(par)
                m[par] = node
            
            if isleft == 1:
                if child in m:
                    node.left = m[child]
                else:
                    node.left = TreeNode(child)
                    m[child] = node.left
            else:
                if child in m:
                    node.right = m[child]
                else:
                    node.right = TreeNode(child)
                    m[child] = node.right
                    
            childs.add(child)
        
        #jo b parent childs me nhi hai mtlb kisi ka baccha nhi hai root hai 
        root = None
        for par, _, _ in descriptions:
            if par not in childs:
                root = m[par]
                break
        return root
            