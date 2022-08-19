class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        available = Counter(nums)
        want = defaultdict(int)
        
        #first person would always start with new group, as it cant be in existing one
        for num in nums:
            if available[num] <= 0:
                continue
            
            #try to get in existing one, but if anyone wants me then
            if want[num] > 0:
                available[num] -= 1
                want[num] -= 1
                
                want[num+1] += 1
            
            #lets start our own group but if only i can have three mor people wit me
            elif available[num] > 0 and available[num+1] > 0 and available[num+2] > 0:
                available[num] -= 1
                available[num+1] -= 1
                available[num+2] -= 1
                
                want[num+3] += 1
            
            #no one wants me, neither i can start a company ah sad
            else:
                return False
            
        return True
            
            
        
        