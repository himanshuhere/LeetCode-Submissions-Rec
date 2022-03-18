Find last_occ: last occurences for each letter in our string
Initialize our stack either as empty or with symbol, which is less than any letter ('!' in my case), so we do not need to deal with the case of empty stack. Also initialize Visited as empty set.
Iterate over our string and if we already have symbol in Visited, we just continue.
Then, we try to remove elements from the top of our stack: we do it, if new symbol is less than previous and also if last occurence of last symbol is more than i: it means that we have removed symbol later in our string, so if we remove it we will not fail to constract full string.
Append new symbol to our stack and mark it as visited.
Finally, return string built from our stack.