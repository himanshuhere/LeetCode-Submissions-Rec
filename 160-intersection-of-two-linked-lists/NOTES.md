* **Brute force** : Do two while loop, pick a node from list1 and then compare it with all nodes in list2 and see if find.
TC : O(M*N), SC : O(1)
* **Hashing** : Use hash to store all nodes aof list1, then iter list2 and check if already present in hashtable.
TC : O(M+N), SC : O(M, N)
* **Optimized 1** : Do iter on each list and find lenght of both, say l1 and l2, thn find the diff bw lenght and, move the longest list head/dummy to diff plus, then both head or dummy wud be of same lenght from intersection, now do iter simntsly on both and check if matches.
TC : O(M) + O(M-N) + O(N) = O(2M)
SC : O(1)
* **Optimized 2** :  same complexity, but small and concise code. So use this approach.
So we will put dummies to heads, and start moving untill one reached null, so longer list wud still have the difference nodes left. so again if d1 reaches the end, put d1 on head2 or vice versa if d2 reaches null. we ll do it for both, and after that both dummy will come at same length and then start checking if nodes have intersection. see code and try to understand. it will work for lists having no intersection also.
See the code in compiler
TC :  O(2M)
SC : O(1)
//boundary check
if(headA == null || headB == null) return null;
ListNode a = headA;
ListNode b = headB;