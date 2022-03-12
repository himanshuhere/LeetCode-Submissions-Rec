**PLS Understand**
​
**If s1[i] == s2[j]**,
then we dont need to count ay operation just move. Its lil common sense to think there movements while doing String Matching DP problem.
**Else**,
1.     ***f(i, j-1) - INSERT***, because hypothetically we are inserting any char ahead of i and then it is (i+1) so (i+1) matched with j, since we hypothetically inserted same char to match. Now one operation done, so we move back to i-1, j-1 as chars matches and we dont need to do any op when they matches, BUT since new char inserted ahead of i, we never really inserted it was hypotheical scene so i will be standing at there only(Hyp. i to i+1 then i-1 so at i only). So [i, j-1] + 1
2.    *** f(i-1, j) - DELETE***, since i and j dont match we tend to delete i, so we deleted hypothetically so we should now move to i-1, as i is deleted right. But j will be there as it only move back once it matches none else. So [i-1, j]+ 1
3.     ***f(i-1, j-1) - REPLACE***, since i and j dont match we have once power to make i same as j, so they matches and we both move back with one more operation count. So, [i-1, j-1] + 1
**BASE CASES**, for string matching DP, there can be two possible case, Either s1 gets exhausted or s2 gets exhausted. So imagin here s1 gets exh, so i==-1, and assume j is still soemwhere in s2, so we need how many operatio to make ***"" to "row"***(example), we need to insert remaining s2 in empty string. Thus*** j+1 insert ***operations
1.     Base case 2, if s2 gets exhausted so means ***"roc" to ""***, thus we need i+1 delete operation on s2 to make s1, ***return i+1***
2.     Both empty, "" "", will be covered in first base case with return as 0