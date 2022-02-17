# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        #brute comverting list to arr first
        # arr = []
        # cur = head
        # while cur:
        #     arr.append(cur.val)
        #     cur = cur.next
        # r = [0]*len(arr)
        # st = []
        # for i in range(len(arr)):
        #     while st and arr[st[-1]] < arr[i]:
        #         prev_ind = st.pop()
        #         r[prev_ind] = arr[i]
        #     st.append(i)
        # return r
        
        #2 wihtout converting, but you need calc lenght as need to initialize arr(prev_ind)
#         n = 0
#         cur = head
#         while cur:
#             n += 1
#             cur = cur.next
            
#         cur = head
#         r = [0]*n
#         st = []
#         i = 0
#         while cur:
#             while st and st[-1][1] < cur.val:
#                 prev_ind = st.pop()[0]
#                 r[prev_ind] = cur.val
#             st.append((i, cur.val))
#             i += 1
#             cur = cur.next
#         return r
    
        #3 without cal lenght, issue was we need right size initialization, lets see hack without lrnght
        
        cur = head
        r = []              #hack
        st = []
        i = 0
        while cur:
            r.append(0)         #hack, wow created space
            while st and st[-1][1] < cur.val:
                prev_ind = st.pop()[0]
                r[prev_ind] = cur.val
            st.append((i, cur.val))
            i += 1
            cur = cur.next
        return r
        