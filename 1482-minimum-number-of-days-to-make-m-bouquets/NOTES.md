class Solution:
def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/769703/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
#BS -TEMPLATE
def feasible(days) -> bool:
bonquets, flowers = 0, 0
for bloom in bloomDay:
if bloom <= days:
flowers += 1
if flowers >= k:
bonquets += flowers // k
flowers %= k
else:
flowers = 0
return bonquets >= m
​
if len(bloomDay) < m * k:
return -1
left, right = min(bloomDay), max(bloomDay)      #obious you can only bloom on given days range only, so min is the first day flower any flower say will bloom and after max no flower can bloom at least at this given list garden
while left < right:
mid = left + (right - left) // 2
if feasible(mid):
right = mid
else:
left = mid + 1
return left