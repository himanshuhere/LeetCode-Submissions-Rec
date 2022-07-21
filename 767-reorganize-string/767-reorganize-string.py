#First thought, keep a counter well yes. And take the most freq char then the sec most fre then third and carry on. Once everything done, repeat process. Okay lets see for aaabbc, we took a - ab - abc - abca - abcab - abcaba -  cool. 
#Lets see for aaabc -> a, ab, abc, abc aa nope didnt work right. 
#Idea is to go like same, with lil trick that pick the most freq and append to answer now since we cant take this char again hold it somewhere and chose the diff one most freq and then put the earlier one because now we can take that, just decrement the count and keep going.
#Use heap

class Solution:
    def reorganizeString(self, S: str) -> str:
        
        res, c = [], Counter(S)
        maxHeap = [(-value,key) for key,value in c.items()]
        heapq.heapify(maxHeap)
        
        preCnt, preChr = 0, ''
        while maxHeap:
            cnt, chr = heapq.heappop(maxHeap)
            res += [chr]
            if preCnt != 0:      #maxheap so it should be neg
                heapq.heappush(maxHeap, (preCnt, preChr))
            cnt += 1            #maxHeap so dec means inc here
            preCnt, preChr = cnt, chr
            
        res = ''.join(res)
        if len(res) < len(S): 
            return ""
        return res