#-ve values string me -5-6-7 ese jayegi to dhyan rakhna hai isliye separator chaiye hota

#bc khud se code kiya negative handle kiya, but pls know bfs too
#DFS
class Codec:
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
    
    
    
        
#BFS
# class Codec:

#     def serialize(self, root):
#         if not root:    return ""
        
#         s, q = "",  deque([root])
#         while q:
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 if node:
#                     s += str(node.val) + "/"
#                 else:
#                     s += "#/"
#                 if node:
#                     q.append(node.left)
#                     q.append(node.right)
#         return s
        

#     def deserialize(self, data):
#         if not data:    return None
        
#         s = data.split('/')
#         i = 0
        
#         root = TreeNode(s[0])
#         q = deque([root])
#         while q:
#             for _ in range(len(q)):
#                 node = q.popleft()

#                 i += 1
#                 if s[i] == "#":
#                     node.left = None
#                 else:
#                     node.left = TreeNode(s[i])
#                     q.append(node.left)

#                 i+=1
#                 if s[i] == "#":
#                     node.right = None
#                 else:
#                     node.right = TreeNode(s[i])
#                     q.append(node.right)

#         return root
        
        

# # Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))