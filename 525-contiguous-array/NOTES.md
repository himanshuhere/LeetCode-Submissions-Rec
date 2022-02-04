​
My idea is very similar to others, but let me try to explain it more visually. My thought was inspired by 121. Best Time to Buy and Sell Stock.
​
Let's have a variable count initially equals 0 and traverse through nums. Every time we meet a 0, we decrease count by 1, and increase count by 1 when we meet 1. It's pretty easy to conclude that we have a contiguous subarray with equal number of 0 and 1 when count equals 0.
​
What if we have a sequence [0, 0, 0, 0, 1, 1]? the maximum length is 4, the count starting from 0, will equal -1, -2, -3, -4, -3, -2, and won't go back to 0 again. But wait, the longest subarray with equal number of 0 and 1 started and ended when count equals -2. We can plot the changes of count on a graph, as shown below. Point (0,0) indicates the initial value of count is 0, so we count the sequence starting from index 1. The longest subarray is from index 2 to 6.
​
![](https://leetcode.com/uploads/files/1487543036101-figure_1.png)
​
From above illustration, we can easily understand that two points with the same y-axis value indicates the sequence between these two points has equal number of 0 and 1.
​
Another example, sequence [0, 0, 1, 0, 0, 0, 1, 1], as shown below,
​
![](https://leetcode.com/uploads/files/1487543760956-figure_2.png)
​
[0, 1, 1, 0, 1, 1, 1, 0],
![](https://leetcode.com/uploads/files/1487544408978-figure_3.png)
​
def findMaxLength(self, nums):
count = 0
max_length=0
table = {0: 0}
for index, num in enumerate(nums, 1):
if num == 0:
count -= 1
else:
count += 1
​
if count in table:
max_length = max(max_length, index - table[count])
else:
table[count] = index
​
return max_length