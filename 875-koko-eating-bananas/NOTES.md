#first test case is sorted and asking for k means heap means sorting means binary search(proof solid ho jata hai jab ordering of indices dsnt matter and it is not here) so see
#brute force: so as per ques it is sure len(piles) <= h, means h can be not less than lenght that means consider idf koko eat max(piles) at one go it is sure max(piles) is going to be ans. but we want mininmum as ques asked slow. so start from min range to max range. what is min. 1 yes koko min can eat one bananana ans max wud be max(piles). (remember max(piles) as max range we are deciding on basis of h constraint given else max would have been more also)
#brute is to go from [1..max(piles)] check for each, the first valid ans wud be ans as it is min. TCS = O(max(P) * len(p))
#same concept coulf be used using binary search and wud save time. TCS = O(log(max(p)) * len(p))
def feasible(k):
hour = 0
for p in piles:
hour += ceil(p/k)
return hour <= h
#BS
lo, hi = 1, max(piles)
while lo < hi:
mid = lo + (hi - lo)//2
if feasible(mid):
hi = mid
else:
lo = mid + 1
return lo