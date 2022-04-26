class DisjointSet:
def __init__(self, n):
self.parent = [i for i in range(n)]
self.rank = [0 for _ in range(n)]
​
def union(self, a, b):
pa = self.find(a)
pb = self.find(b)
if pa == pb: return
if self.rank[pa] > self.rank[pb]:
self.parent[pb] = pa
elif self.rank[pa] < self.rank[pb]:
self.parent[pa] = pb
else:
self.parent[pa] = pb
self.rank[pb] += 1
​
def find(self, a):
if self.parent[a] == a:
return a
​
self.parent[a] = self.find(self.parent[a])  #recursion
return self.parent[a]
​
class Solution:
def minCostConnectPoints(self, points: List[List[int]]) -> int: