A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
b
a
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
b = null, then b = a1
b                   a = null, then a = b1
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
b
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
a
b
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
a
b
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
a
b = null
A:     a1 → a2 → a3 → a4 → null
B:     b1 → b2 → b3 → null
a = null
Since a == b is true (both refer to null), end loop while(a != b), return a = null.
​
Notice that if list A and list B have the same length, this solution will terminate in no more than 1 traversal; if both lists have different lengths, this solution will terminate in no more than 2 traversals -- in the second traversal, swapping a and b synchronizes a and b before the end of the second traversal. By synchronizing a and b I mean both have the same remaining steps in the second traversal so that it's guaranteed for them to reach the first intersection node, or reach null at the same time (technically speaking, in the same iteration) -- see Case 2 (Have Intersection & Different Len) and Case 4 (Have No Intersection & Different Len)