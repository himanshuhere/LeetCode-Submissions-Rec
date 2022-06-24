The % prevents the TLE from the case (e.g., target=[10000000, 1]) where the largest element is significantly bigger than the sum of other elements.
​
For example, target = [max, a1, a2]. Here are the steps in backtracking:
​
Subtract the rest of the array from the largest number, we have target = [max-(a1+a2), a1, a2].
But the value of max is so large, that max-(a1+a2) is still the largest number in the array.
So we continue to subtract from the largest number, and we have a new array target = [max-2*(a1+a2), a1, a2].
But the value of max is so large, that max-2*(a1+a2) is still the largest number in the array.
Repeat 1-4...
​
After n iterations, we have a new array target = [max-n*(a1+a2), a1, a2], where max-n*(a1+a2) is not the largest any more.
​
Can we accelerate the process?
Yes.
We have max-n*(a1+a2) = max % (a1+a2). That is how the % works.
​
For example, target = [10, 3].
Without %, we have [10, 3] -> [7, 3] -> [4, 3] -> [1, 3].
With %, we have [10, 3] -> [10 % 3, 3] = [1, 3] quickly.
​
Note that max % (a1+a2) == 0 is a special case. For example, target = [10000000, 1]. If we perform max % (a1+a2), we will end with target = [0, 1]. We use if-else to deal with this special case, as shown in other top-voted answers.