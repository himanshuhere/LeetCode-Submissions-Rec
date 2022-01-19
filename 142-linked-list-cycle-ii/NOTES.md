* **brute force**: Use hashtable
* **Best Intuition** : Do find cycle in LL using slow and fast then, where they meet start moving from there one step with the dummy from head one step, they are bound to move at cycle begininng point.
See, this algo is not imp but its intuition is. Thats what is going to be asked. Make sure u understand this intuition before code. O(n), no space
Consider the following linked list, where E is the cylce entry and X, the crossing point of fast and slow.
H: distance from head to cycle entry E
D: distance from E to X
L: cycle length
_____
/     \
head_____H______E       \
\       /
X_____/
If fast and slow both start at head, when fast catches slow, slow has traveled H+D and fast 2(H+D).
Assume fast has traveled n loops in the cycle, we have:
2H + 2D = H + D + L  -->  H + D = nL  --> H = nL - D
Thus if two pointers start from head and X, respectively, one first reaches E, the other also reaches E.
In my solution, since fast starts at head.next, we need to move slow one step forward in the beginning of part 2