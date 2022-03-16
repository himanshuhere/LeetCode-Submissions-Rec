class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        i = 0
        n = len(popped)
        for ele in pushed:
            st.append(ele)
            while i < n and st and popped[i] == st[-1]:
                st.pop()
                i += 1
        return len(st) == 0
                