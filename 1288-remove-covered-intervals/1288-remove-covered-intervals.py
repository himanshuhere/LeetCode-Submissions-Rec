class Solution:
    def removeCoveredIntervals(self, inter: List[List[int]]) -> int:
        # inter = sorted(inter)
        # print(inter)
        # c=0
        # for i in range(len(inter)-1):
        #     if inter[i][0] <= inter[i+1][0] and inter[i][1] <= inter[i+1][1]:
        #         continue
        #     c += 1
        # return c
        #just like other intervals problem i ddi till today. first key basis me sort karke kaam ho jata tha. merge me second key ko running time maintain karte the while me min dekhte hu min hi rakhte the.
        #is ques me actual me issue ye hai ki [3,6] cover hota hai [2,8], me but [[5, 12], [0, 10]]
#isme nhi chal rha
#actually first key ko sort karna hai normal and jab first key same hai second key ko sort karna hai dec order me, to hamesha covered one covering k pehle hi ayega, ek loop laga do bas
#now since first key increasing me sorted hai toh, starting point ko to check karna hi nhi hahi, bas ending point ka khyal rakhna hai see if 2--3--4--5, if starting sorted like this means i+1 is always coverd by i(starting point of view se), now if you see to cover 1,6 by 3,4. start[i] <= start[i+1] yes but for end point ots opposite, end[i] >= end[i+1]. so when start point is sorted make sure to sort end like decreasing.. iske bad we just need one traversal. chose prev as first, then keep checking. (we ll skip start as its always sorted <=)
        
        inter = sorted(inter, key=lambda x:(x[0], -x[1]))
        culprits = 0
        prev = inter[0]       #end
        for i in range(1, len(inter)):
            if prev[1] >= inter[i][1]:
                culprits += 1
            else:
                prev = inter[i]
        return len(inter) - culprits