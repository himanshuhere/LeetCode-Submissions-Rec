# No longer need to visit this node's partner values ever again,
# so let's remove all of it's partner values.
# This also stops the partner nodes from visiting each other again
# As that is a possibility (You visit all 100s, then when you are visiting
# the next 100 in your graph, you have to iterate through all 100s again,
# that is inefficient so we empty the 100s connections)
del m[arr[i]]       #or m[arr[i]] = []
res += 1
# if we don't get an answer, return -1. Not needed as we are guaranteed an answer but some error checking is a best practice so why not
return -1