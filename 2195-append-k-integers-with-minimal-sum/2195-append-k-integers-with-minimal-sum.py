class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        #ks=[]
        nums=sorted(nums)
        ans=0
        print(nums)
        for i in range(len(nums)):
            if i==0: 
                if nums[0] > 1:
                    if k < nums[0]:
                        ans+=(k*(k+1)//2)
                        k=0
                        break
                    else:
                        tmp=nums[0]-1
                        ans+=(tmp*(tmp+1)//2)
                        k-=tmp
            else:
                if nums[i-1]+1==nums[i] or nums[i-1]==nums[i]:    
                    continue
                last = nums[i-1]
                pre = last*(last+1)//2
                if k <= nums[i]-nums[i-1]-1:
                    kk=nums[i]-(nums[i]-nums[i-1]-k)
                    cur = (kk*(kk+1)//2)
                    ans+=(cur-pre)
                    k=0
                    break
                else:
                    t=nums[i]-1
                    cur=(t*(t+1)//2)
                    k-=(nums[i]-nums[i-1]-1)
                    ans+=(cur-pre)
            
        if k>0:
            last = nums[-1]+1
            ans += (last*k)
            k-=1
            ans+=(k*(k+1)//2)
            
        return ans
                