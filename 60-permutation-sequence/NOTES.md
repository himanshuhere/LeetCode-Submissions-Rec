* **Brute Force** : Use recusrion and generate all the permutaion on n list. Put each permutation in a list adn then at last sort the list and return k-1th index value of list.
TC : n! *x* n *x* n!logn! == Hell lot of time. Think something other than gen all perm use some optimization to cut the steps.
* **Optimal** : TC : n^2
I'm sure somewhere can be simplified so it'd be nice if anyone can let me know. The pattern was that:
​
say n = 4, you have {1, 2, 3, 4}
​
If you were to list out all the permutations you have
​
1 + (permutations of 2, 3, 4)
​
2 + (permutations of 1, 3, 4)
​
3 + (permutations of 1, 2, 4)
​
4 + (permutations of 1, 2, 3)
​
​
We know how to calculate the number of permutations of n numbers... n! So each of those with permutations of 3 numbers means there are 6 possible permutations. Meaning there would be a total of 24 permutations in this particular one. So if you were to look for the (k = 14) 14th permutation, it would be in the
​
3 + (permutations of 1, 2, 4) subset.
​
To programmatically get that, you take k = 13 (subtract 1 because of things always starting at 0) and divide that by the 6 we got from the factorial, which would give you the index of the number you want. In the array {1, 2, 3, 4}, k/(n-1)! = 13/(4-1)! = 13/3! = 13/6 = 2. The array {1, 2, 3, 4} has a value of 3 at index 2. So the first number is a 3.