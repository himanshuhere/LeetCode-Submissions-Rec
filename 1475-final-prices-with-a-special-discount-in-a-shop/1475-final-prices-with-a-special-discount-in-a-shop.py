class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #nlr
        r = [None]*len(prices)
        st = []
        for i in range(len(prices)-1, -1, -1):
            while st and prices[st[-1]] > prices[i]:
                st.pop()
            r[i] = prices[st[-1]] if st else 0      #discount
            st.append(i)
        
        for i in range(len(prices)):
            prices[i] -= r[i]
        return prices
        
            