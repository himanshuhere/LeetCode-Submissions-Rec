# can we move one forward?, if we can then let's try that
if (i+1) not in visited:
q.append(i+1)
# can we move one back? if we can then let's try that
if (i-1) not in visited and (i-1) >= 0:
q.append(i-1)
​
# let's add every possible value that has the same value as the current one to our list to visit
for neighbor in m[arr[i]]:
if neighbor in visited:
continue
q.append(neighbor)
# No longer need to visit this node's partner values ever again,
# so let's remove all of it's partner values.
# This also stops the partner nodes from visiting each other again
# As that is a possibility (You visit all 100s, then when you are visiting
# the next 100 in your graph, you have to iterate through all 100s again,
# that is inefficient so we empty the 100s connections)
m[arr[i]] = []
res += 1
# if we don't get an answer, return -1. Not needed as we are guaranteed an answer but some error checking is a best practice so why not
return -1