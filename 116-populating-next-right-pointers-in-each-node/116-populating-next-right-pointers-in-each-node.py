class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #easy peasy but hard on LC IB so see pepcoding video pls pls noice ques and acha 
        #or do BFS and same logic instead of external while do bfs and internal logic same i meant think lil. Bas you have to think of attaching links while u on root so rrot then attach left and right dont think like u r on same level and do same level links using parent no, on parent connect childs then go childs
        if not root:
            return None
        #1
        head = root
        while head.left:
            x = head
            while x:
                x.left.next = x.right
                if x.next:
                    x.right.next = x.next.left
                x = x.next
            head = head.left
        return root
        
        #bfs
        if root == None: return None

        q = deque([root])
        while q:
            prev = None
            for _ in range(len(q)):
                curr = q.popleft()
                if prev:       #har level ka pehla node prev=none hoga, uske alag conncection bangea
                    prev.next = curr
                prev = curr

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return root

    #We can follow the same BFS approach. The only difference is that while traversing a level we will remember the previous node to connect it with the current node.