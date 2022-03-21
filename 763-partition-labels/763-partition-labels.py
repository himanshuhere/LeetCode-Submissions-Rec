class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #Record the last occurence of every character in the string
        lastocc = [0]*26
        for i, ch in enumerate(s):
            lastocc[ord(ch)-ord('a')] = i
            
        ans = []
        n = len(s)
        i = 0
        pre = 0
        while i < n:
            
            #Get the last index of this char in s
            last = lastocc[ord(s[i])-ord('a')] 
            
            #You cannot get shorter window than this, so now only option left is to remain same/expand more.
            #Check every char in the window, if anyone has their last occurence outside of current window. if yes expand current window and keep checking
            j = i
            while j < n and j <= last:
                if lastocc[ord(s[j])-ord('a')] > last:
                    last = lastocc[ord(s[j])-ord('a')]
                j += 1   
            
            #Loop will break when we are done with checking all element ans this is our finaly window size, answer should be have the window size, thus this step - >
            #pre = sum(ans)
            ans.append((last-pre)+1)
            pre += ans[-1]
            i = j
        return ans