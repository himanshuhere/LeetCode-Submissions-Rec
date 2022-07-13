# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:    return ""
        
        s, q = "",  deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    s += str(node.val) + "/"
                else:
                    s += "#/"
                if node:
                    q.append(node.left)
                    q.append(node.right)
        return s
        

    def deserialize(self, data):
        if not data:    return None
        s = data.split('/')
        i = 0
        
        root = TreeNode(s[0])
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                i += 1
                if s[i] == "#":
                    node.left = None
                else:
                    node.left = TreeNode(s[i])
                    q.append(node.left)

                i+=1
                if s[i] == "#":
                    node.right = None
                else:
                    node.right = TreeNode(s[i])
                    q.append(node.right)

        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))