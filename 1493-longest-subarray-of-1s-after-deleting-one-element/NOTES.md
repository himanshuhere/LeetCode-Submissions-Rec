#variable sliding window
ones = 0
ans = 0
i, j = 0, 0
while j < len(nums):
if nums[j] == 0:
ones+=1
if ones <= 1:
ans = max(ans, j-i)
else:
while ones > 1:
if nums[i] == 0:
ones -= 1
i+=1
j+=1
return ans