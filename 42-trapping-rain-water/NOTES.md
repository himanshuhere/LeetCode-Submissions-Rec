*please see all solutions here this will build your more understading about basuc prefix n suffix operation which can be useful in single pass or greedy*
​
* **Approach 1: Brute force**
Do as directed in question. For each element in the array, we find the maximum level of water it can trap after the rain, which is equal to the minimum of maximum height of bars on both the sides minus its own height.
​
Algorithm
​
```
Initialize ans=0ans=0
Iterate the array from left to right:
Initialize *leftmax=0* and *rightmax=0*
Iterate from the current element to the beginning of array updating:
* leftmax=max(leftmax, height[j])*
Iterate from the current element to the end of array updating:
*rightmax=max(rightmax,height[j])*
Add *min(leftmax,rightmax)−height[i] * to *ans*
```
​
​
​
Complexity Analysis
Time complexity: O(n^2)
Space complexity: O(1)'