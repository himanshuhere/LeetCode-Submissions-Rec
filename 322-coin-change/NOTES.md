class Solution:
def coinChange(self, coins: List[int], amt: int) -> int:
#1
@lru_cache(None)
def dp(amt):
if amt == 0:
return 0
if amt < 0:
return math.inf
if amt in m:
return m[amt]
ans = math.inf
for coin in coins:
#if amt >= coin: if this then remove second base condition
ans = min(ans, dp(amt - coin) + 1)
m[amt] = ans
return ans
m={}
ans = dp(amt)
return ans if ans != math.inf else -1
#2 - if sec parameter is itself array coins y create 2d use both
d = [math.inf] * (amt+1)
d[0] = 0