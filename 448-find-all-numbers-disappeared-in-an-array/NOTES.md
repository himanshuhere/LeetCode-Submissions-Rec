#simple cyclic sort dikha kare jab b ye range 1-n array ki ho.
#try out, after cyclic sort, all culpprits will have wrong position. karke ikatthe dedo bc
#CYCLIC SORT
n = len(nums)
i = 0
while i < n:
j = nums[i] - 1                             #correct index for this number
if nums[i] != nums[j]:
nums[i], nums[j] = nums[j], nums[i]     #swap
else:
i += 1
#print(nums) #when we ll put all of ele at their right position repeatings will have random pos, no not random. our ans position actually . all repeat will be at wrong pos, just figure out thos
ans = []
for i in range(n):
if nums[i] - 1 != i:
ans.append(i+1)
return ans