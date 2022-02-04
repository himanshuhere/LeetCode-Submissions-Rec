#n = len(nums)-1
# return abs( (n*(n+1))//2 - sum(nums)) nah dint work for more than 2 duplicates
#came up with diff approach of marking see if works hope
for i in range(len(nums)):
if nums[abs(nums[i])] < 0:           #negative/marked/visited
return abs(nums[i])                   #duplicate
else:
nums[abs(nums[i])] = -nums[abs(nums[i])]  #mark it