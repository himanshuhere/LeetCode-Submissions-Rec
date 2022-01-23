#recursion
#constraint 10^9
#         l = [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,
#             12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,
#             12345678,23456789,123456789]
#         ans = []
#         for li in l:
#             if li >= low and li <= high:
#                 ans.append(li)
#         return ans
#2
#         def f(n):
#             if low <= n <= high:
#                 res.append(n)
#                 return
#             if n > high:
#                 return
#             last = n%10
#             if last < 9:
#                 f(n*10 + (last+1))
#         res = []
#         for i in range(1, 10):
#             f(i)
#         return res
#3 bfs
arr = [x for x in range(1, 10)]
q = deque(arr)
res = []
while q:
x = q.popleft()
if low <= x <= high:
res.append(x)
last_num = x % 10
if last_num != 9:
q.append(x * 10 + last_num + 1)
return res