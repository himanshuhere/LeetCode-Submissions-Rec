# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #lenght one
        def one():
            m, n = 0, 0
            cura, curb = headA, headB
            while cura:
                m += 1
                cura = cura.next
            while curb:
                n += 1
                curb = curb.next

            #diff in etra dist is abs(m-n)
            diff = abs(m-n)

            if m > n:
                while diff:
                    headA = headA.next
                    diff -= 1
            else:
                while diff:
                    headB = headB.next
                    diff -= 1

            #now travel at same rate
            while headA != headB:
                headA = headA.next
                headB = headB.next
            return headA
        
        def twoPointer():
            if not headA or not headB:  return None #see notes best one
            a, b = headA, headB
            while a != b:
                if not a:
                    a = headB
                else:
                    a = a.next
                
                if not b:
                    b = headA
                else:
                    b = b.next
            return a
        
        def optimized():
            pass
            #go find any one tail and connect it to its head.
            #now send thid head to find the begginnning of cycle fucntion, thats your ans.
            #make sure to remove the created cycle.
            #o(n)
        return twoPointer()

