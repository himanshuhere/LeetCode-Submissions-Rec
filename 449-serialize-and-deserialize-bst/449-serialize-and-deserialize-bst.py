# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
#BT serialize to o(n) preorder any order mar do
#but BST me b pre k bad optimized INORDER
#this is brute tho pre but i dont understand inorder me konsa time kam lag rha

    def serialdfs(self, root):
        if not root:
            return "N"
        return str(root.val) +'/'+ self.serialdfs(root.left) +'/'+ self.serialdfs(root.right)
    
    def desdfs(self, data):
        if data[self.i] == 'N':
            return None
        
        root = TreeNode(data[self.i])
        
        self.i += 1
        root.left = self.desdfs(data)
        self.i += 1
        root.right = self.desdfs(data)
        return root
        
    def serialize(self, root):
        s = self.serialdfs(root)
        print(s)
        return s
        
    def deserialize(self, data):
        data = data.split('/')
        self.i = 0
        return self.desdfs(data)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans