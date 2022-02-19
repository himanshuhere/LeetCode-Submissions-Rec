class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        #bahut pyara ques, contest me nhi bana, adha bana aage ka soch hi paye test case3 me atak gye.
        #see notes for algo
        
        if finalSum % 2 == 1:
            return []
        
        
        ans = []
        ev = 2
        curSum = 0
        
        while curSum + ev <= finalSum:
            ans.append(ev)
            curSum += ev
            ev += 2
        
        if curSum == finalSum:
            return ans
        
        ans[-1] += finalSum - curSum
        return ans