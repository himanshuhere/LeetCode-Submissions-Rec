Consider the following boundaries for the element x
left ......... mid ......... mid + k ......... right
​
x <= arr[mid]
arr[mid + k] <= x
arr[mid] < x < arr[mid + k]
* Case 1 : x <= arr[mid]
If x is less than arr[mid] then it's clear that arr[mid + k] cannot be a part of our output k elements. This is because there are k + 1 elements between arr[mid] and arr[mid + k] inclusive. So, the start will either be mid or towards the left of it.
​
* Case 2 : arr[mid + k] <= x
Similar to previous case, arr[mid] cannot be a part of our output k elements because of the k + 1 elements we have in between. Therefore, start will lie towards the right of mid
​
* Case 3 : arr[mid] < x < arr[mid + k]
This is more like a combination of the above two cases.
​
A. If x is closer to arr[mid] then just like our case 1, arr[mid + k] cannot be a part of our output k elements. Therefore, our start will either be mid or towards the left of it.
​
B. If x is closer to arr[mid + k], then just like case 2, arr[mid] cannot be a part of our output k elements, which means that our start will lie towards the right of mid.
​
Let's implement this
​
def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
low = 0
high = len(arr) - k
while low < high:
mid = low + (high-low)//2
if x<=arr[mid]:
high=mid