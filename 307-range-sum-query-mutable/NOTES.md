else:
mid = root.lx + (root.rx-root.lx)//2
if index<=mid:
root.left = updateTree(root.left,index,value)
root.sum = root.left.sum+root.right.sum
else:
root.right = updateTree(root.right,index,value)
root.sum = root.left.sum+root.right.sum
return root
```
Step 3: Range Queries
Given a range [i,j] we want to return the sum of the interval [i,j]
​
Range Queries are the simplest part of the bunch. We check for three kinds of overlaps:
​
1. Case 1(Complete Overlap): Root interval [lx,rx] completely lies inside interval [i,j]. In this case we return root.sum.
​
2. Case 2(No Overlap): Root interval [lx,rx] and [i,j] are disjoint sets. Return 0 in this case.
3. Case 3(Partial Overlap): [lx,rx] and [i,j] have partial overlap. Note that, here [i,j] lying completely inside of [lx,rx] is also considered partial overlap.
​
```
def checkOverlap(nodeInterval,queryInterval):
ix,iy = nodeInterval
jx,jy = queryInterval
if ix>=jx and iy<=jy:
return 0 #complete overlap
elif iy<jx or ix>jy:
return 1 #no overlap
else:
return 2 #partial overlap
​