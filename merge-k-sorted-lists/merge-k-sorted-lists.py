
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #         The above solution works fine with Python 2.However, with Python3 it gives Type Error:
        # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
        # This error occurs because the cmp() special method is no longer honored in Python 3

        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        h = []
        head = tail = ListNode(0)
        for i in lists:
            if i:
                heapq.heappush(h, (i.val, i))

        while h:
            node = heapq.heappop(h)[1]
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(h, (node.next.val, node.next))

        return head.next
    
        # lheap = []
        # for i in lists:
        #     heapq.heappush(lheap,(i.val, i))
        # dummy = ListNode(None)
        # cur = dummy
        # while lheap:
        #     node = heapq.heappop(lheap)[-1]
        #     cur.next = node
        #     cur = cur.next
        #     if node.next:
        #         heapq.heappush(lheap,(node.next.val,node.next))
        # return dummy.next
    
    
#         if not lists:
#             return None
#         if len(lists) == 1:
#             return lists[0]
#         mid = len(lists) // 2
#         l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
#         return self.merge(l, r)
    
#     def merge(self, l, r): #l and r are two list tho l and r are working as head1 and head2 for both list
#         dummy = p = ListNode()
#         while l and r:
#             if l.val < r.val:
#                 p.next = l
#                 l = l.next
#             else:
#                 p.next = r
#                 r = r.next
#             p = p.next
#         p.next = l or r
#         return dummy.next
        
#         #2
#         nodes = []
        
#         head = point = ListNode(0)
        
#         for l in lists:
#             while l:
#                 nodes.append(l.val)
#                 l = l.next
#         for x in sorted(nodes):
#             point.next = ListNode(x)
#             point = point.next
#         return head.next
#     #(NlogN