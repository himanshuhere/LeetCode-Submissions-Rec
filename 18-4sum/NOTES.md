* just like two sum, we have to pick and hold three ele first then search for fourth one using target - (p1 + p1 + p1) but that wud lead us to O(n^3 * n) = O(n^4).
* To save lil, time we can pick three ele then can apply Binary search than linear. but for than we need to sort the array first. Thus
* **Brute Force - Sort -> 3 ptrs + BS ==> Hash table** : So first put i, j , k at index 0, 1 ,2 then start searching for target - (p1+p2+p3) in rem list using BS then add the result to hashtable to maintain uniqueness. Move k till it reach n then j++ and k=j+1 then after j reach n same with i
TS: O(N^3*LOGN), SC: o(N) Hashset
*  Now **Optimized**, (SORT FIRST)wud be to use alog where we put two pointers at 0, 1 and then we apply two pointers left and right to remaining sorted list. left wud be j+1 or p2+1 and right wud be at last and they will start moviebg towards theirself and finding the remainig two and when found they ll return but since the array is sorted and there might be same elemenets next to each other, other time also they can find the same ele and that wud be a duplicate quad but we have a hashset to handle that NOO, we are not using hashset in this lets optimize it more using constant space. How? we will skip the duplicate elements next to each otehr for left and right, left moving right and right moving left,, you see when we write login to skip duplicates for left right aur say jump to next uniqe ele that wud save us hashset.
1  1    4     6  6  6  7  8  9  9     9
i    j   left  ->                     <- right
then
1  1    4     6       6  6  7      8       9   9  9
i    j          left  ->        <- right     //see strivers exp yt
finally after left right cross move j++ and when j is done with list then i++
But, for i and j movement same thing to take care like left and right, we have to skip duplicates and jump to new ele
when j moves i will stay at same place but when j is done with list we gonna move i to new ele and then j wud come back to i+1 and will start again his ope till reaches n and then same i++ and j = I + 1 and again till i reaches n but dont worry two for loop for i and j wud handle all incriment u just take care duplicates skiping and j repositionafter i ++
TS : o(N^3) SP : o(1)
Yes we need to take a list to push quads there to return but that dosent count in SP because thats ques req to return.