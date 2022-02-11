class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
                #return list(permutations(A))

        n = len(nums)
        res = []
        
        def dfs( nums, ind, n):
            if ind == n:
                res.append(nums.copy())
                return 

            for i in range(ind, n):
                if i > ind and nums[i] == nums[ind]: continue
                nums[ind], nums[i] = nums[i], nums[ind]
                dfs(nums.copy() , ind+1, n)
                
        nums.sort()
        dfs(nums, 0, len(nums))
        return res
