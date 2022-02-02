AKA, the general idea to find some max is to go through all cases where max value can possibly occur and keep updating the max value. The efficiency of the scan depends on the size of cases you plan to scan.
To increase efficiency, all we need to do is to find a smart way of scan to cut off the useless cases and meanwhile 100% guarantee the max value can be reached through the rest of cases.
​
In this problem, the smart scan way is to set two pointers initialized at both ends of the array. Every time move the smaller value pointer to inner array. Then after the two pointers meet, all possible max cases have been scanned and the max situation is 100% reached somewhere in the scan. Following is a brief prove of this.
​
#Two edge pointer + Greedy movement of pointers
l, r = 0, len(height) - 1
area = 0
while l < r:                     #l<=r, wil work too, thing practical, woudl one piller make sence?
if height[l] < height[r]:
area = max(area, (r-l)*height[l])   #r-l = width, smaller height
l += 1                              #r is bigger, move l might get bigger area next (greed)
else:
area = max(area, (r-l)*height[r])
r -= 1
return area