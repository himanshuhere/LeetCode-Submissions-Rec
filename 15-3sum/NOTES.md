* **Brute Force** : Run 3 loops, for: i = 0 to n-1 ==> for: j = i+1 to n-1 ==> for: k = j+1 to n-1: find i + j + k ==0, but we need unique triplets so maintain a set with unique values.
TC : n^3logm : logm for set insertion, SC : n
//Unordered set best insertion time is o(1) but worst is (log n), similary ordered set has log n in all cases.
​
* ** Hashing ** : run a loop put ele and count in hashset, then run two loops, pick i and j and check for -(i+j) as, a+b+c=0, c = -a-b..make sure c or k u r finding in hash shoud be have correct count as if a or b ==c then remov eone count from hash for a b then consider c. see strivers sol
* **Two pointer** : SORT the array, we ll pick a using one loop for list, then after picking a i ll apply kind of binary search to next i+1 to n -1 list, using two pointers for b and c and will find the duo satisfies b + c = -a, if if found then move b++, c-- but since we dont want to use space for uniqueness we ll jump same duplicates again to maintain uniqness, untill j k crossess, same with a for jumping duplicates. See code to understand more.
TC : N^2, SC = 1 , ONLY LIST TO RETURN RESULT.